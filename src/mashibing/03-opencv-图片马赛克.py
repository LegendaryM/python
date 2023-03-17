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
img = cv2.imread(r'./attachment/bai.jpg')
gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)
face_detector = cv2.CascadeClassifier(r'./attachment/haarcascade_frontalface_alt.xml')

faces = face_detector.detectMultiScale(gray)
for x, y, w, h in faces:
    face = img[y:y + h, x:x + w]
    img[y:y + h, x:x + w] = cv2.resize(face[::10, ::10], dsize=(w, h))

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


