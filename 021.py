#coding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencv-logo.png')
ret,img=cv2.threshold(img,250,255,cv2.THRESH_BINARY_INV)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2=img.copy()
#ret,img = cv2.threshold(img,127,255,0)

image, contours = cv2.findContours(img2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#print contours
#img2 = cv2.drawContours(img, contours, -1, (0,255,0), 3)

plt.subplot(221),plt.imshow(img),plt.title('One'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(img2),plt.title('Three'), plt.xticks([]), plt.yticks([])
#plt.subplot(222),plt.imshow(img2),plt.title('Two'), plt.xticks([]), plt.yticks([])

plt.show()