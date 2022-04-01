# @File  : CameraCatching.py
# @Date  :  2021/05/13

# 利用自己的摄像头做一个入侵检测程序。当有比较大异物进入摄像头内时，
# 自动截图保存在指定的文件夹中。

import cv2
# 创建摄像头
cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,800) #设置分辨率
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,600)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # 逐帧捕获
    ret, frame = cap.read()
    if not ret:
        break;
    # 转化成灰度图像
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # 图像的平滑
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 1)
    # 图像的边缘检测
    img_candy = cv2.Canny(img_blur, 50, 100)
    imglll = img_candy.copy()
    contours, hierarchy = cv2.findContours(imglll, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow("11",imglll)
    img_res = frame.copy()
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        area = w*h
        print(area)
        if area > 10000:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
# 完成所有操作后，释放捕获器
cap.release()
cv2.destroyAllWindows()

