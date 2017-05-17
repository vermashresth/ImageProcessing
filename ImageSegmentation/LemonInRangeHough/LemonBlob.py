# -*- coding: utf-8 -*-
"""
Created on Tue May 16 21:40:23 2017

@author: Shresth
"""

import cv2
import numpy as np;
 
# Read image
img = cv2.imread("Lemons3.jpg")

hsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
#Filter by green color
yellow = np.array([20,0,0])
green=np.array([50,255,255])
    
mask=cv2.inRange(hsv, yellow, green)
res=cv2.bitwise_and(img, img, mask=mask)



resgrey=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
th3 = cv2.adaptiveThreshold(resgrey,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

th3=cv2.medianBlur(th3,3 )
cv2.imshow('blur',th3)
cv2.waitKey(0   )
 
# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create()
 
# Detect blobs.
keypoints = detector.detect(th3)
 
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)