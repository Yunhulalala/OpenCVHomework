# @File  : 6AutomaticScoring.py
# @Author: Zeng Yixuan
# @Date  :  2021/05/18
# 6，请将答题卡反转成正面并将卡片内容单独做成一副图像。
import cv2
import numpy as np

img = cv2.imread("images/card.png", 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 高斯模糊
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# 边缘检测
edged = cv2.Canny(blurred, 75, 200)
# 轮廓检测
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
# 复制图像
contours_img = img.copy()
cv2.drawContours(contours_img, cnts, -1, [0, 0, 255], 3)
cv2.imshow('contours_img',contours_img)
# 确保检测到了轮廓
if len(cnts)>0:
    # 根据轮廓大小进行升序排序
    cnts = sorted(cnts,key=cv2.contourArea,reverse=True)
    # 遍历每一个轮廓
    for c in cnts:
        peri = cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,0.02*peri,True)
        # approx 点集为4 四边形
        if len(approx)==4:
            docCnt = approx
            break
pts = docCnt.reshape(4, 2)
rect = np.zeros((4, 2), dtype=np.float32)
# 点的x+y求和
s = np.sum(pts, axis=1)
# 答题卡的左上角点的位置
rect[0] = pts[np.argmin(s)]
# 答题卡的右下角点的位置
rect[2] = pts[np.argmax(s)]
# 点的y-x
diff = np.diff(pts, axis=1)
# # 答题卡的右上角点的位置
rect[1] = pts[np.argmin(diff)]
# 答题卡的左下角点的位置
rect[3] = pts[np.argmax(diff)]
# 获取答题卡四个角的坐标点
tl, tr, br, bl = rect
# 计算输入的w和h值
widthA = np.sqrt(((br[0]-bl[0]) ** 2) + ((br[1]-bl[1]) ** 2))
widthB = np.sqrt(((tr[0]-tl[0]) ** 2) + ((tr[1]-tl[1]) ** 2))
maxWidth = max(int(widthA), int(widthB))

heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
maxHeight = max(int(heightA), int(heightB))
# 变换后对应坐标位置,
dst = np.array([[0, 0],
               [maxWidth-1, 0],
               [maxWidth-1, maxHeight-1],
               [0, maxHeight-1]], dtype=np.float32)
# 透视变换
H = cv2.getPerspectiveTransform(rect, dst)
warped = cv2.warpPerspective(gray, H, (maxWidth, maxHeight))
cv2.imshow('warped',warped)
while(1):
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()