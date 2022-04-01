import cv2
import matplotlib.pyplot as plt

# 显示不同类型的图像
img = cv2.imread("images/lena.jpg", 1)
img_RGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_GRAY = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

plt.subplot(2,2,1);plt.imshow(img);plt.axis('off');plt.title('img')
plt.subplot(2,2,2);plt.imshow(img_RGB);plt.axis('off');plt.title('RGB')
plt.subplot(2,2,3);plt.imshow(img_GRAY);plt.axis('off');plt.title('GRAY')
plt.subplot(2,2,4);plt.imshow(img_HSV);plt.axis('off');plt.title('HSV')
plt.show()

# 提取RGB通道
# img = cv2.imread("lena.jpg",1)
# img_copy = img.copy()
# img_copy[:, :, 0] = 0
# img_copy[:, :, 1] = 0
# img_copy[:, :, 2] = 0
# cv2.imshow('image',img_copy)
# key = cv2.waitKey(0) & 0xFF
# if key == 27: # 按下Esc退出
#     cv2.destroyAllWindows()
# elif key == ord('s'): # 保存退出
#     cv2.imwrite('lena2.png', img_copy)   # 另存为
#     cv2.destroyAllWindows()
