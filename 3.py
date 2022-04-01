import cv2
import numpy as np

# 创建黑色图像
img = np.zeros((512,512,3), np.uint8)
# 直线
img_copy1 = img.copy()
cv2.line(img_copy1,(0,511),(511,0),(2,122,10),10)
# 矩形
img_copy2 = img.copy()
cv2.rectangle(img_copy2,(10,10),(200,200),(255,0,0),3)
# 圆
img_copy3 = img.copy()
cv2.circle(img_copy3,(255,255),100,(0,255,255),3,3)
# 椭圆
img_copy4 = img.copy()
cv2.ellipse(img_copy4,(255,255),(100,50),180,0,180,(255,255,0),3,3,3)
# 给图像添加文本
img_copy5 = img.copy()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img_copy5, 'HHHHHHH', (50, 50), font,1,(255,255,255),1)
cv2.imshow('image',img_copy5)
cv2.waitKey(0)
cv2.destroyAllWindows()