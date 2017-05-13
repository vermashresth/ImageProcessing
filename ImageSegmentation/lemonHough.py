# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:17:55 2017

@author: Shresth
"""
import time
import cv2
import numpy as np
a=time.clock()
im=cv2.imread("lemon.jpeg"  )
cv2.imshow('orig',im)
imgray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

th3 = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

th3=cv2.medianBlur(th3,3)
circles = cv2.HoughCircles(th3,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=20,maxRadius=80)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(im,(i[0],i[1]),i[2],(0,255,0),2)
    
    # draw the center of the circle
    cv2.circle(im,(i[0],i[1]),2,(0,0,255),3)
b=time.clock()
print b-a
cv2.imshow('detected circles',im)

cv2.waitKey(0)

cv2.destroyAllWindows()