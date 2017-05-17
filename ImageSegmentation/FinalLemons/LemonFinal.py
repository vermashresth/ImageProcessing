# -*- coding: utf-8 -*-
"""
Created on Wed May 17 18:33:31 2017

@author: Shresth
"""

import cv2
import numpy as np

img=cv2.imread("lemons2.jpg" )

hsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
#Filter by green color
yellow = np.array([20,100,100]) #[20,0,0 for dark setting]
green=np.array([50,255,255])
    
mask=cv2.inRange(hsv, yellow, green)
res=cv2.bitwise_and(img, img, mask=mask)


resgrey=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)

#apply adaptive threshold 

th3 = cv2.adaptiveThreshold(resgrey,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

#invert
th3=cv2.bitwise_not(th3)
cv2.imshow('threshold',th3)
cv2.waitKey(0)

#find contours
im2, contours, hierarchy = cv2.findContours(th3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
c2=[]
#filter out small contours by area
for i in contours:
    area = cv2.contourArea(i)
    if area>80:
        epsilon = 0.0001*cv2.arcLength(i,True)
        approx = cv2.approxPolyDP(i,epsilon,True)
        c2.append(approx)
        print(area)
        
        
# create new image with only contours and blur it using mean blur
a=np.zeros(img.shape,np.uint8)
cv2.drawContours(a, c2, -1, (255,255,255), 1)
a=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
a=cv2.bitwise_not(a)
kernel = np.ones((5,5),np.float32)/25
#
#a=cv2.bitwise_not(a)
a = cv2.filter2D(a,-1,kernel)
cv2.imwrite("c2.jpeg",a)
cv2.imshow('fin',a)
cv2.waitKey(0)


# dilate and close this new image
a=cv2.imread("c2.jpeg")
cv2.imshow('read',a)
cv2.waitKey(0)
k=np.ones((3,3),np.uint8)
dil=cv2.dilate(a,k)
clo = cv2.morphologyEx(dil, cv2.MORPH_CLOSE, k)
cv2.imshow('read',clo)
cv2.waitKey(0)

gr=cv2.cvtColor(clo,cv2.COLOR_BGR2GRAY)

#find hough circles
circles = cv2.HoughCircles(gr,cv2.HOUGH_GRADIENT,1,35,
                            param1=50,param2=35,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))

#filter out circles in a fixed range
a=[i for i in circles[0,:] ]
for i in  circles[0,:]:
    # draw the outer circle
    if i[2]<58 and i[2]>15 :
       
        cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
        #print(i[2])
        # draw the center of the circle
        cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
print "No of lemons : ", len(circles[0,:])
cv2.imshow('final',img)
cv2.waitKey(0)
cv2.imwrite("lemon2result.jpeg",img)
cv2.destroyAllWindows()