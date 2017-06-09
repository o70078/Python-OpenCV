import cv2
import numpy as np

# 读取一张照片
frame = cv2.imread('009.jpg')
frame=cv2.resize(frame,(600,400))
#转换到HSV
hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#设定蓝色的阈值
lower_blue=np.array([110,50,50])
upper_blue=np.array([130,255,255])

#根据阈值构建掩模
mask=cv2.inRange(hsv,lower_blue,upper_blue)

#对原图像和掩模进行位运算
res=cv2.bitwise_and(frame,frame,mask=mask)

#显示图像
cv2.imshow('frame',frame)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.waitKey()

#关闭窗口
cv2.destroyAllWindows()