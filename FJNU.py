# @File  : FJNU.py
# @Date  :  2021/05/11
import cv2
import numpy as np
src = cv2.imread("FJNU.jpg",1)
imgInfo = src.shape
height = imgInfo[0]
width = imgInfo[1]
print(height,width)
cv2.imshow('image',src)
mask = src.copy()
mask[:] = 0
font = cv2.FONT_HERSHEY_SIMPLEX
mask = cv2.putText(mask,"Fujian Normal University", (width-250, height-20), font, 0.5, (255, 255, 255))
mask = cv2.bitwise_not(mask)
mask = cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
des = cv2.bitwise_and(src,src,mask=mask)
cv2.imshow('pic',mask)
cv2.imshow('Final',des)
cv2.waitKey(0)
