#coding:utf-8
"""
Created on Fri Jan 10 20:25:00 2014
@author: duan 
"""
import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(1):
    #获取每一帧
    ret,frame=cap.read()
    rows,cols,L=frame.shape

    #这里的第一个参数为旋转中心，第二个为旋转角度，第三个为旋转后的缩放因子
    #可以通过设置旋转中心，缩放因子，以及窗口大小来防止旋转后超出边界的问题
    M1=cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
    #第三个参数是输出图像的尺寸中心
    dst=cv2.warpAffine(frame,M1,(2*cols,2*rows)) 
    
    #平移
    M2=np.array([[1,0,200],[0,1,0]],dtype=np.float32)
    dst1=cv2.warpAffine(frame,M2,(800,600))

    #仿射变换
    pts1=np.float32([[50,50],[200,50],[50,200]])
    pts2=np.float32([[10,100],[200,50],[100,250]])
    M3=cv2.getAffineTransform(pts1,pts2)
    dst2=cv2.warpAffine(frame,M3,(cols,rows))

    #透视变换
    pts1 = np.float32([[0,0],[cols,0],[0,rows],[cols,rows]])
    pts2 = np.float32([[30,0],[cols,30],[0,rows-30],[cols-30,rows]])
    M4=cv2.getPerspectiveTransform(pts1,pts2)
    dst3=cv2.warpPerspective(frame,M4,(cols,rows))

    #显示图像
    cv2.imshow('frame',frame)
    #cv2.imshow('dst',dst)
    #cv2.imshow('dst1',dst1)
    #cv2.imshow('dst2',dst2)
    cv2.imshow('dst3',dst3)
    k=cv2.waitKey(5)&0xFF
    if k==ord("1"): break
    #关闭窗口
cv2.destroyAllWindows()