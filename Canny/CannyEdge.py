# -*- coding: utf-8 -*-
"""
Created on Sat May 13 00:41:18 2017

@author: Shresth
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('aasf.jpg',0)
img=cv2.medianBlur(img,11)
edges = cv2.Canny(img,30,100,40,3,True)


plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
