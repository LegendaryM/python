# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: 01-opencv人脸识别.py
@time: 2023/3/16 15:12
"""

import cv2

# img是matrix矩阵, 三维: 高、宽、数据(452. 867, 3)
img = cv2.imread(r'./attachment/liu.jpg')
gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)
# 级联算法 图片中找特征，满足一部分特征，算作人脸
face_detector = cv2.CascadeClassifier(r'./attachment/haarcascade_frontalface_alt.xml')

# 检测人脸： 坐标，左上角坐标(x,y), 宽度，高度
faces = face_detector.detectMultiScale(gray)
for x, y, w, h in faces:
    # cv2.rectangle(img,  # 标记图片
    #               pt1=(x, y),  # 左上角
    #               pt2=(x+w, y+h),  # 右下角
    #               color=[0, 0, 255],
    #               thickness=2)   # 线宽
    cv2.circle(img,
               center=(x + w//2, y + h//2),  # 圆心
               radius=h//2,            # 半径
               color=[0, 0, 255],      # 颜色
               thickness=2)    # 线宽

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


