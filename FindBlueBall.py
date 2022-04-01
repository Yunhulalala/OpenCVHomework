# 1,请从colorball.png图像中找出蓝色球，最后画出一幅只显示蓝色球的图像。
# 提示，通过色彩空间的转化将BGR图像转化到HSV空间后进行。通过滚动条动态
# 选取蓝色的在hsv颜色空间的上界和下界，通过cv.inrange确定最后要选取的范围。
#
# 2，做一个升级版的调色板，双击鼠标切换所画图形的形状，并在右上角用文字标明下次所画的形状。


import cv2

import numpy as np

import matplotlib.pyplot as plt

img = cv2.imread('colorball.png')
# 转化成HSV图像
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 定义颜色范围，h：100~124 S：43~255 V：46：255 为蓝色的范围
lower_color = np.array([100, 43, 46])
upper_color = np.array([124, 255, 255])
# 获取掩映，将hsv在范围之外的值变成0
mask = cv2.inRange(hsv, lower_color, upper_color)
# 图像按位与，当像素值不为0不做操作，当像素为0时直接做0处理
res = cv2.bitwise_and(img, img, mask=mask)
# cv2的颜色系统时BGR，所以还要转化成RGB图像
# must convert BGR to RGB
imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
resrgb = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
img_data = [imgrgb, hsv, mask, resrgb]
titles = ['Original image', 'HSV image', 'Mask image', 'Result image']
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(img_data[i])
    plt.title(titles[i])
plt.show()
