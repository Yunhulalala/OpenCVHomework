# @File  : car.py
# @Date  :  2021/05/13

# 请将图中汽车的车牌区域用绿色方框标出
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Car_number_plate.jpg",1)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# 轮廓检测前图像需要经过灰度化和二值化
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 图像的模糊，高斯滤波
img_blur = cv2.GaussianBlur(img_gray,(5,5),1)
# 图像的边缘检测
img_candy = cv2.Canny(img_blur,50,100)
contours, hierarchy = cv2.findContours(img_candy.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
img_res = img.copy()
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area>3000:
        peri = cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,0.02*peri,True)
        obj_corners = len(approx)
        if obj_corners == 4:
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(img_res,(x,y),(x+w,y+h),(0,255,0),3)
img_data = [img,img_candy,img_res]
titles = ["Original", "candy", "Result"]
for i in range(3):
    plt.subplot(2,2,i+1)
    plt.imshow(img_data[i])
    plt.title(titles[i])
plt.show()
