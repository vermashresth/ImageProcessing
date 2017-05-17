# -*- coding: utf-8 -*-
"""
Created on Wed May 17 14:51:03 2017

@author: Shresth
"""
import cv2
import numpy as np
img=cv2.imread('lemons2.jpg')
print img
a=cv2.imread("cont2.jpeg")
cv2.imshow('read',a)
cv2.waitKey(0)
k=np.ones((3,3),np.uint8)
dil=cv2.dilate(a,k)
clo = cv2.morphologyEx(dil, cv2.MORPH_CLOSE, k)
cv2.imshow('read',clo)
cv2.waitKey(0)

gr=cv2.cvtColor(clo,cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gr,cv2.HOUGH_GRADIENT,1,35,
                            param1=50,param2=35,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))


a=[i for i in circles[0,:] ]
for i in  circles[0,:]:
    # draw the outer circle
    if i[2]<58 and i[2]>15 :
       
        cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
        print(i[2])
        # draw the center of the circle
        cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
"""

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# noise removal

kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)

# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.2*dist_transform.max(),255,0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
cv2.imshow('dd',sure_bg)

# Marker labelling
ret, markers = cv2.connectedComponents(thresh)

# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown==255] = 0
       
       
markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]
"""
cv2.imshow('final',img)
cv2.waitKey(0)
cv2.destroyAllWindows()