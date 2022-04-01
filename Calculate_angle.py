# @File  : Calculate_angle.py
# @Date  :  2021/05/18

import cv2
import numpy as np
def drawCircle(event, x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),2,(0,0,255),-1)
        point = (x,y)
        pointList.append(point)
img = cv2.imread("angel.jpg",1)
pointList = []
cv2.namedWindow('image')
cv2.setMouseCallback('image',drawCircle)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
print(pointList)
# 斜率1
k1 = abs(pointList[0][0]-pointList[1][0])/abs(pointList[0][1]-pointList[1][1])
# 斜率2
k2 = abs(pointList[1][0]-pointList[2][0])/abs(pointList[2][1]-pointList[3][1])
# 斜率3

print(k1)