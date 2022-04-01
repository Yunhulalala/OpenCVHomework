# @File  : ShowInOneWindow.py
# @Date  :  2021/05/11
import cv2
def show_in_one_window(image_list,layout,image_scale=0.6):
    # 根据布局中的图的个数，找出图片
    (rows,colums) = layout
    show_image_list =image_list[0:rows*colums]
    # 将图片转化成指定的大小
    resized_image_list = [cv2.resize(i,None,)]