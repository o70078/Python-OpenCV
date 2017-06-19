#coding=utf-8
import cv2
import numpy as np
import math
import random

class annet:
    #输入节点数
    InCount=0;
    #隐层节点数
    HideCount=0;
    #输出节点数
    OutCount=0;
    #样本总数
    SampleCount=0;
    #输入节点的输入数据
    x=np.array([],dtype=np.float64);
    #隐含节点的输出
    x1=np.array([],dtype=np.float64);
    #输出节点的输出
    x2=np.array([],dtype=np.float64);
    #隐含层的输入
    o1=np.array([],dtype=np.float64);
    #输出层的输入
    o2=np.array([],dtype=np.float64);
    #权值矩阵w
    w=np.array([[]],dtype=np.float64);
    #权值矩阵v
    v=np.array([[]],dtype=np.float64);
    #学习率
    rate=0.0;
    #隐含层阈值矩阵
    b1=np.array([],dtype=np.float64);
    #输出层阈值矩阵
    b2=np.array([],dtype=np.float64);
    #隐层阈值矩阵
    db1=np.array([],dtype=np.float64);
    #输出层阈值矩阵
    db2=np.array([],dtype=np.float64);
    #输出层误差
    pp=np.array([],dtype=np.float64);
    #隐含层误差
    qq=np.array([],dtype=np.float64);
    #输出层的教师数据
    yd=np.array([],dtype=np.float64);
    #均方误差
    e=0;
    #归一化比例系数
    in_rate=0;
    def ComputeHideCount(self,m,n):
        s = math.sqrt(0.43 * m * n + 0.12 * n * n + 2.54 * m + 0.77 * n + 0.35) + 0.51;
        ss = int(s);
        if (s - ss) > 0.5:
             ss+=1;
        return int(ss);

    def __init__(self, p1,t1):
        self.InCount=p1[0].size;
        self.OutCount=t1[0].size;
        self.SampleCount = p1.shape[0];
        self.HideCount=self.ComputeHideCount(self.InCount,self.OutCount);
        print("输入节点数目：" + str(self.InCount));
        print("隐层节点数目：" + str(self.HideCount));
        print("输出层节点数目：" + str(self.OutCount));
        self.x = np.zeros(self.InCount);
        self.x1 = np.zeros(self.HideCount);
        self.x2 = np.zeros(self.OutCount);
        self.o1 = np.zeros(self.HideCount);
        self.o2 = np.zeros(self.OutCount);

        self.dw = np.zeros([self.InCount, self.HideCount]);
        self.dv = np.zeros([self.HideCount, self.OutCount]);

        self.b1 = np.zeros(self.HideCount);
        self.b2 = np.zeros(self.OutCount);
        self.db1 = np.zeros(self.HideCount);
        self.db2 = np.zeros(self.OutCount);

        self.pp = np.zeros(self.HideCount);
        self.qq = np.zeros(self.OutCount);
        self.yd = np.zeros(self.OutCount);
        #init w,v
        self.w = (np.random.random([self.InCount, self.HideCount])[:,:] * 2 - 1.0) / 2;
        self.v = (np.random.random([self.HideCount, self.OutCount])[:,:] * 2 - 1.0) / 2;

        self.rate = 0.8;
        self.e = 0.0;
        self.in_rate = 1.0;
        return;
    
    def train(self,p,t):
        self.e = 0.0;
        #get p，t max
        self.in_rate = np.max([np.max(np.fabs(p)),np.max(np.fabs(t))]);
        for isamp in range(self.SampleCount):
            #self.x=[p[isamp,i] for i in range(self.InCount)]/self.in_rate;
            # self.yd=[t[isamp,i] for i in range(self.InCount)]/self.in_rate;

            #数据归一化
            self.x=p[isamp,:]/self.in_rate;
            self.yd=t[isamp,:]/self.in_rate;

            self.o1[:]=0.0;
            self.o2[:]=0.0;

            #计算隐层的输入和输出
            for j in range(self.HideCount):
                for i in range(self.InCount):
                    self.o1[j]+=self.w[i][j] * self.x[i];
                self.x1[j] = 1.0 / (1.0 + math.exp(-self.o1[j] - self.b1[j]));

            #计算输出层的输入和输出
            for j in range(self.OutCount):
                for i in range(self.HideCount):
                    self.o2[j]+=self.v[i][j] * self.x1[i];
                self.x2[j] = 1.0 / (1.0 + math.exp(-self.o2[j] - self.b2[j]));

            #计算输出层误差和均方差
            self.qq[:] = (self.yd[:] - self.x2[:]) * self.x2[:] * (1.0 - self.x2[:]);
            self.e = np.sum((self.yd[:] - self.x2[:]) * (self.yd[:] - self.x2[:]));
            for j in range(self.OutCount):
                for i in range(self.HideCount):
                     self.v[i][j] += self.rate * self.qq[j] * self.x1[i];#update v

            #计算隐层误差
            self.pp[:]=0.0;
            for j in range(self.HideCount):
                for i in range(self.OutCount):
                    self.pp[j]+=self.qq[i] * self.v[j][i];
                self.pp[j] *= self.x1[j] * (1 - self.x1[j]);
                for i in range(self.InCount):
                    self.w[i][j] += self.rate * self.pp[j] *self.x[i];#update w
                
            #update b2
            self.b2=self.rate * self.qq[:];
			#update b1
            self.b1=self.rate * self.pp[:];

        self.e=math.sqrt(self.e);
        return; 
    
    def sim(self,p):
        self.x=[p[i]/self.in_rate for i in range(self.InCount)]
        self.o1[:]=0.0;
        self.o2[:]=0.0;

        for j in range(self.HideCount):
            for i in range(self.InCount):
                self.o1[j] += self.w[i][j] * self.x[i];
            self.x1[j] = 1.0 / (1.0 + math.exp(-self.o1[j] - self.b1[j]));

        for k in range(self.OutCount):
            for j in range(self.HideCount):
                self.o2[k] += self.v[j][k] * self.x1[j];
            self.x2[k] = 1.0 / (1.0 + math.exp(-self.o2[k] - self.b2[k]));
            
        self.x2[:] = self.x2[:]*self.in_rate;
        return self.x2;

if __name__ == "__main__":

    #构建一个神经网络
    an=annet(np.zeros([20,3]),np.zeros([20,1]));

    #提供三千次数据给神经网络学习
    for i in range(3000):
        #生成20组数字(每组3个)
        p1=np.random.randint(30,150,[20,3]);#np.zeros([20,3]);
        
        #用算法计算答案
        t1=np.zeros([20,1]);
        t1[:,0]=(p1[:,0]*0.8) + p1[:,1] - (p1[:,2]/2);

        #让神经网络学习
        an.train(p1,t1);

    #看看神经网络有没有学会我的算法
    testdata=np.array([66,74,82]);
    print "正确答案:" + str((testdata[0]*0.8) + testdata[1] - (testdata[2]/2));
    print "神经网络算出的答案:" + str(an.sim(testdata));