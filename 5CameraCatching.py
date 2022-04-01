# @File  : CameraCatching.py
# @Date  :  2021/05/13

# 利用自己的摄像头做一个入侵检测程序。当有比较大异物进入摄像头内时，
# 自动截图保存在指定的文件夹中。

import cv2
import time
import datetime

# 创建摄像头
cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,800) #设置分辨率
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,600)

count = 0
# 上一帧图像
lastframe = None
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # 逐帧捕获
    ret, frame = cap.read()
    if not ret:
        break;
    # 转化成灰度图像
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 高斯模糊
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 1)
    # 显示处理后的图像
    if lastframe is None:
        lastframe = img_blur
        continue
    # cv2.imshow('frame2', img_gray)
    # 计算当前图像于当前图像的区别
    frameDelta = cv2.absdiff(img_gray, lastframe)
    # cv2.imshow("diff",frameDelta)
    # 二值化图像
    thresh = cv2.threshold(frameDelta, 45, 255, cv2.THRESH_BINARY)[1]
    # cv2.imshow('thresh', thresh)

    # 对二值图像进行轮廓检测
    contours, hierarchy = cv2.findContours(thresh, cv2.cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 1000:
            count += 1
            # 保存图像
            cv2.imwrite("D:\\AAPROJECT\\PythonProject\\OpenCVHomeWork\\InvadingVision\\" + str(count) + ".jpg", frame)
    lastframe = img_blur
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
# 完成所有操作后，释放捕获器
cap.release()
cv2.destroyAllWindows()
