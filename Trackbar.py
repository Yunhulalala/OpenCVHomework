import cv2
import numpy as np

def nothing(x):
    pass
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')
# 创建RGB三个滚动条
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
# 创建开关
cv2.createTrackbar('on//off','image',0,1,nothing)
while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    r=cv2.getTrackbarPos('R','image')
    g=cv2.getTrackbarPos('G','image')
    b=cv2.getTrackbarPos('B','image')
    swtich = cv2.getTrackbarPos('on//off','image')
    if swtich == 0:
        img[:] = 0
    elif:
        img = [b, g, r]
cv2.destroyAllWindows()
