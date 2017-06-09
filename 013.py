#coding:utf-8
import numpy as np
import cv2

cap=cv2.VideoCapture(0)
#cap=cv2.VideoCapture("C:\Users\o7007\Videos\OH.mp4")

'''
fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)  
size = (int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.cv.CV_FOURCC('I','4','2','0')  
print cap.isOpened()
'''
while(True):
    ret,frame=cap.read()
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #cv2.circle(frame,(128,128),63,(0,0,255),3)
    #cv2.putText(frame,"this is made in opencv",(0,300),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,128,128),2)
    #frame[:,:,0:2]=0
    frame[15:22,15:100]=[100,200,140]
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('1'):break
cap.release()
cv2.destroyAllWindows()