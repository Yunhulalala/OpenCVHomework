# @File  : Calculate_angle.py
# @Date  :  2021/05/18
# 3，计算图中两个角度的值
import cv2
import math

def drawCircle(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 2, (0, 0, 255), -1)
        point = (x, y)
        pointList.append(point)


img = cv2.imread("images/angle3.jpg", 1)
pointList = []
cv2.namedWindow('image')
cv2.setMouseCallback('image', drawCircle)
while (1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
# 斜率1
k1 = (pointList[0][0] - pointList[1][0]) / (pointList[0][1] - pointList[1][1])
# 斜率2
k2 = (pointList[2][0] - pointList[1][0]) / (pointList[2][1] - pointList[1][1])
# 斜率3
k3 = (pointList[3][0] - pointList[4][0]) / (pointList[3][1] - pointList[4][1])
# 斜率4
k4 = (pointList[5][0] - pointList[4][0]) / (pointList[5][1] - pointList[4][1])
angle1 = 180 / (3.14 / (math.atan((k1 - k2) / (1 + k1 * k2))))
angle2 = 180 / (3.14 / (math.atan((k3 - k4) / (1 + k3 * k4))))
# 保存小数点后两位
angle1 = round(angle1, 2)
angle2 = round(angle2, 2)
print(angle1, angle2)
