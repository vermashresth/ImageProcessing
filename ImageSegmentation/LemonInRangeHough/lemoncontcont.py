# -*- coding: utf-8 -*-
"""
Created on Wed May 17 15:38:49 2017

@author: Shresth
"""

import cv2 
import numpy as np

img=cv2.imread("cont.jpeg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('ff',img)
cv2.waitKey(0)
ret,thresh = cv2.threshold(img,20,255,0)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#print(contours)
#cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow('aa',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()