# -*- coding: utf-8 -*-
"""
Created on Mon May 08 04:49:44 2017

@author: Shresth
"""

import numpy as np
import cv2

img=cv2.imread("Lemons3.jpg"  )
hsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
#Filter by green color
yellow = np.array([20,0,0])
green=np.array([50,255,255])
    
mask=cv2.inRange(hsv, yellow, green)
res=cv2.bitwise_and(img, img, mask=mask)

imgray=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imgray,50,200,cv2.THRESH_BINARY_INV)
print(thresh)
th3 = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
th3=cv2.medianBlur(th3,3)
ret, tho = cv2.threshold(imgray,80,255,cv2.THRESH_BINARY_INV)
im2,contours, heirarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(th3, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('1',tho)
cv2.waitKey(0)
# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(tho,cv2.MORPH_OPEN,kernel, iterations = 2)
# sure background area
cv2.imshow('o',opening)
cv2.waitKey(0)
sure_bg = cv2.dilate(opening,kernel,iterations=3)
# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

#cv2.imshow('aa',sure_fg)
#cv2.waitKey(0)
# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)
# Add one to all labels so that sure background is not 0, but 1
markers = markers+1
# Now, mark the region of unknown with zero

markers[unknown==255] = 0
markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]
print markers
#cv2.imshow('aaa',im)
#cv2.waitKey(0)


"""circles = cv2.HoughCircles(th3,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=20,maxRadius=80)

circles = np.uint16(np.around(circles))
print (circles)
print "heyy"
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(im,(i[0],i[1]),i[2],(0,255,0),2)
    
    # draw the center of the circle
    cv2.circle(im,(i[0],i[1]),2,(0,0,255),3)
"""
cv2.imshow('detected circles',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

