# -*- coding: utf-8 -*-
"""
Created on Wed May 17 14:51:03 2017

@author: Shresth
"""
import cv2
import numpy as np
img=cv2.imread('Lemons3.jpg')
a=cv2.imread("cont.jpeg")
cv2.imshow('read',a)
cv2.waitKey(0)
k=np.ones((3,3),np.uint8)
dil=cv2.dilate(a,k)
clo = cv2.morphologyEx(dil, cv2.MORPH_CLOSE, k)
cv2.imshow('read',clo)
cv2.waitKey(0)

gr=cv2.cvtColor(clo,cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gr,cv2.HOUGH_GRADIENT,1,35,
                            param1=50,param2=40,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))


a=[i for i in circles[0,:] ]
for i in  circles[0,:]:
    # draw the outer circle
    if i[2]<58 and i[2]>20 :
       
        cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
        print(i[2])
        # draw the center of the circle
        cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
        
cv2.imshow('final',img)
cv2.waitKey(0)
cv2.destroyAllWindows()