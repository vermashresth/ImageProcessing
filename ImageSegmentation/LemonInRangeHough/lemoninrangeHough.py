# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:17:55 2017

@author: Shresth
"""
import time
import cv2
import numpy as np
a=time.clock()
img=cv2.imread("lemon.jpeg" )

hsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
#Filter by green color
yellow = np.array([20,0,0])
green=np.array([50,255,255])
    
mask=cv2.inRange(hsv, yellow, green)
res=cv2.bitwise_and(img, img, mask=mask)



resgrey=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)

#apply adaptive threshold and blur

th3 = cv2.adaptiveThreshold(resgrey,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

th3=cv2.medianBlur(th3,3 )


#Detect circles in the image
circles = cv2.HoughCircles(th3,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))

b=time.clock()
print "Time taken: ",b-a, " seconds"
#Draw circles
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    
    # draw the center of the circle
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

print "Number of lemons: ",len(circles[0])
cv2.imshow('greenFilter',res)
cv2.waitKey(0)
cv2.imshow('greyscale',resgrey)
cv2.waitKey(0)
cv2.imshow('threshold',th3)
cv2.waitKey(0)
cv2.imshow('detected circles',img)
cv2.waitKey(0)
cv2.imwrite("GreenFilter.png",res)
cv2.imwrite("greyscale.png",resgrey)
cv2.imwrite("threshold.png",th3)
cv2.imwrite("detected.png",img)


cv2.destroyAllWindows()