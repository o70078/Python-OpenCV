#coding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencv-logo.png')
#cv2.imshow("a",img)
#cv2.waitKey()
#cv2.destroyAllWindows()
kernel = np.ones((5,5),np.float32)/25#卷积
dst = cv2.filter2D(img,-1,kernel)
blur = cv2.blur(img,(5,5))#平均
GaussianBlur = cv2.GaussianBlur(img,(5,5),0)#高斯模糊
median = cv2.medianBlur(img,5)#中值模糊
bilateralFilter = cv2.bilateralFilter(img,9,75,75)#双边滤波

plt.subplot(331),plt.imshow(img),plt.title('Original'),plt.xticks([]), plt.yticks([])
plt.subplot(332),plt.imshow(dst),plt.title('Averaging'),plt.xticks([]), plt.yticks([])
plt.subplot(333),plt.imshow(blur),plt.title('blur'),plt.xticks([]), plt.yticks([])
plt.subplot(334),plt.imshow(GaussianBlur),plt.title('GaussianBlur'),plt.xticks([]), plt.yticks([])
plt.subplot(335),plt.imshow(median),plt.title('median'),plt.xticks([]), plt.yticks([])
plt.subplot(336),plt.imshow(bilateralFilter),plt.title('bilateralFilter'),plt.xticks([]), plt.yticks([])
plt.show()
