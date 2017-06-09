#coding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencv-logo.png',0)

ret,img=cv2.threshold(img,250,255,cv2.THRESH_BINARY_INV)

#cv2.imshow("a",img)
#cv2.waitKey()
#cv2.destroyAllWindows()

kernel = np.ones((10,10),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 2)#腐蚀
dilation = cv2.dilate(img,kernel,iterations = 2)#膨胀
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)#先进性腐蚀再进行膨胀就叫做开运算(用来去除噪声)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)#先膨胀再腐蚀(用来去除物体中的小洞)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)#形态学梯度
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)#礼帽
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)#黑帽


plt.subplot(331),plt.imshow(img),plt.title('Original'),plt.xticks([]), plt.yticks([])
plt.subplot(332),plt.imshow(erosion),plt.title('erosion'),plt.xticks([]), plt.yticks([])
plt.subplot(333),plt.imshow(dilation),plt.title('dilation'),plt.xticks([]), plt.yticks([])
plt.subplot(334),plt.imshow(opening),plt.title('opening'),plt.xticks([]), plt.yticks([])
plt.subplot(335),plt.imshow(closing),plt.title('closing'),plt.xticks([]), plt.yticks([])
plt.subplot(336),plt.imshow(gradient),plt.title('gradient'),plt.xticks([]), plt.yticks([])
plt.show()
