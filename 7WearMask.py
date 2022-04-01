# @File  :7WearMask.py
# @Date  :  2021/05/25
# 7，给图片中的人物戴上口罩。
import dlib
import cv2
import numpy as np

# 初始化dlib的预测器
detector = dlib.get_frontal_face_detector()
landmark_path = r"shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(landmark_path)

# 转变为灰度图
img = cv2.imread("images/xixi.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# """
# 在灰度图像中检测人脸并创建一个对象-存储边界矩形的坐标列表
# 第二个参数中的“1”表示应该向上采样图像1次。
# 这会使图像变得更大，并允许我们检测更多的面孔
# """
faces = detector(img_gray, 1)

# 使用预测器获取外形
img_copy = img.copy()
points = [[]]
for face in faces:
    landmark = predictor(img_gray, face)
    for i in range(68):
        # 获取脸部的67个关键点的位置
        point = (landmark.part(i).x, landmark.part(i).y)
        # cv2.circle(img_copy,point,1,(255,4,12),1)
        if (i >= 2 and i <= 14):
            points[0].append(point)
        if (i == 28):
            points[0].append(point)
print(points)
# 将points列表转化城points数组
points = np.array(points)
print(points)
# 多边形填充
# 第二个参数需要三维数组
cv2.fillPoly(img_copy, points, (238, 194, 17))
cv2.imshow("Origin", img)
cv2.imshow("Detected", img_copy)
cv2.waitKey(0)
