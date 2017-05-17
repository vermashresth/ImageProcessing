# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:41:06 2017

@author: Shresth
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 17 13:15:08 2017

@author: Shresth
"""
  
import time
import cv2
import numpy as np
a=time.clock()
img=cv2.imread("lemons2.jpg" )

hsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
#Filter by green color
yellow = np.array([20,100,100])
green=np.array([50,255,255])
    
mask=cv2.inRange(hsv, yellow, green)
res=cv2.bitwise_and(img, img, mask=mask)



resgrey=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)

#apply adaptive threshold and blur

th3 = cv2.adaptiveThreshold(resgrey,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
"""
n=cv2.medianBlur(th3,11)
#n=cv2.bitwise_not(n)
cv2.imshow('ee',n)
cv2.waitKey(0)
p=cv2.bitwise_and(th3,n)
# p=cv2.bitwise_not(p)
cv2. imshow('aaaa',p)
cv2.waitKey(0)
"""
kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
op = cv2.morphologyEx(th3, cv2.MORPH_CLOSE, kernel)
kernel=np.ones((3,3))
#opening = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
#opening = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
clos=cv2.morphologyEx(op, cv2.MORPH_OPEN, kernel)
#th3=cv2.medianBlur(th3,5)
dil = cv2.dilate(th3,kernel,iterations = 1)

th3=cv2.bitwise_not(th3)
cv2.imshow('ii',th3)
cv2.waitKey(0)
im2, contours, hierarchy = cv2.findContours(th3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
c2=[]
for i in contours:
    area = cv2.contourArea(i)
    if area>70:
        epsilon = 0.0001*cv2.arcLength(i,True)
        approx = cv2.approxPolyDP(i,epsilon,True)
        c2.append(approx)
        print(area)
        (x,y),radius = cv2.minEnclosingCircle(i)
        center = (int(x),int(y))
        radius = int(radius)
        cv2.circle(img,center,radius,(255,0,0),3)
        


a=np.zeros(img.shape,np.uint8)
cv2.drawContours(a, c2, -1, (255,255,255), 1)
a=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
a=cv2.bitwise_not(a)
kernel = np.ones((5,5),np.float32)/25
#
#a=cv2.bitwise_not(a)
a = cv2.filter2D(a,-1,kernel)
cv2.imwrite("cont2.jpeg",a)
cv2.imshow('fin',a)
cv2.waitKey(0)
"""
circles = cv2.HoughCircles(a,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=130)
circles = np.uint16(np.around(circles))

b=time.clock()

#Draw circles
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(a,(i[0],i[1]),i[2],(0,255,0),2)
    
    # draw the center of the circle
    cv2.circle(a,(i[0],i[1]),2,(0,0,255),3)

print "Number of lemons: ",len(circles[0])

cv2.imshow('ff',a)
cv2.waitKey(0)
print "hiiii"
"""
cv2.destroyAllWindows()