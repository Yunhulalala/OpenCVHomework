# @File  : SinglarPic.py
# @Date  :  2021/05/18
# 6请将答题卡反转成正面并将卡片内容单独做成一副图像。
import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),2,(0,0,255),-1)
        position = (x,y)
        pointList1.append(position)
img = cv2.imread("card.png",1)
img2 = img.copy()
cols = 500
rows = 700
pointList1 = []
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
pointList1 = np.float32(pointList1)
pointList2 = np.float32([(0, 0), (cols, 0), (cols, rows), (0, rows)])
M = cv2.getPerspectiveTransform(pointList1, pointList2)
dst = cv2.warpPerspective(img2, M, (cols, rows))
cv2.imshow("dst",dst)
cv2.waitKey(0)

