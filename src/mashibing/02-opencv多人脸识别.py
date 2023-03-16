# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: 01-opencv人脸识别.py
@time: 2023/3/16 15:12
"""

import cv2   # pip install opencv-contrib-python

# img是matrix矩阵, 三维: 高、宽、数据(452. 867, 3)
img = cv2.imread(r'./attachment/suoerwei.jpg')
img = cv2.resize(img, dsize=(2126//2, 1104//2))
gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)
# 级联算法 图片中找特征，满足一部分特征，算作人脸
face_detector = cv2.CascadeClassifier(r'./attachment/haarcascade_frontalface_alt.xml')

# detectMultiScale2返回两个参数，取第一个
# minNeighbors 参数越大，条件越苛刻，参数越小，宽松
# scaleFactor 参数越大，缩放越大，遗漏人脸，参数越小，细腻，找到人脸
# faces = face_detector.detectMultiScale2(gray,
#                                         scaleFactor=1.02,
#                                         minNeighbors=3,
#                                         minSize=(30, 30),
#                                         maxSize=(50, 50))
faces = face_detector.detectMultiScale3(gray, outputRejectLevels=True)

for x, y, w, h in faces[0]:
    cv2.rectangle(img,  # 标记图片
                  pt1=(x, y),  # 左上角
                  pt2=(x+w, y+h),  # 右下角
                  color=[0, 0, 255],
                  thickness=2)   # 线宽

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


