# @File  : jishu.py
# @Author: Zeng Yixuan
# @Date  :  2021/05/21

import cv2
import numpy as np

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        count.append("1")
        print(len(count))
# 创建一个黑色图像，一个窗口，并绑定到窗口的功能
img = np.zeros((512,512,3), np.uint8)
count = []
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()