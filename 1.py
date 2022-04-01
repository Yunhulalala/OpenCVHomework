import cv2
# ---图像的显示与保存---
# img = cv2.imread("lena.jpg",cv2.IMREAD_COLOR)
# cv2.imshow('image',img)#显示图片在屏幕
# key = cv2.waitKey(0) & 0xFF
# if key==27:#按下Esc退出
#     cv2.destroyAllWindows()
# elif key == ord('s'):#保存退出
#     cv2.imwrite('lena2.png',img)   #另存为
#     cv2.destroyAllWindows()

# ---读取摄像头---
# cap = cv2.VideoCapture(0)
# if not cap.isOpened():
#     print("Can't open the camera")
#     exit()
# while True:
#     ret,frame=cap.read()
#     if not ret:
#         print("Can'r recevie frame,Exiting")
#         break
#     # 转化成灰度图像q
#     # 显示结果帧
#     cv2.imshow('frame',frame)
#     if (cv2.waitKey(0) &0xFF) == ord('q'):
#         break
# # 释放摄像机
# cap.release()
# cv2.destroyAllWindows()

# ----读取本地视频----
cap = cv2.VideoCapture('C:/Users/yunhu/Desktop/vedio.mp4')
if not cap.isOpened():
    print("Can't open the camera")
    exit()
while True:
    ret,frame=cap.read()
    if not ret:
        print("Can't recevie frame,Exiting")
        break
    # 转化成灰度图像q
    # 显示结果帧
    cv2.imshow('frame', frame)
    if cv2.waitKey(4) == ord('q'): # 4表示快慢
        break
# 释放摄像机
cap.release()
cv2.destroyAllWindows()