# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: 08-摄像头人脸操作.py
@time: 2023/3/17 15:05
"""

import cv2
# -1表示随机选取一个摄像头, 多个时:0表示第一个摄像头,1表示第二个摄像头
v = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier(r'./attachment/haarcascade_frontalface_alt.xml')
head = cv2.imread(r'./attachment/dog-head.jpg')
while True:
    flag, frame = v.read()
    # 最后一张图片后面，没有图片，无法读取图片，返回False
    if not flag:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 播放慢了，检测人脸耗时操作，扫描整张图片，图片大，耗时长
    faces = face_detector.detectMultiScale(gray)
    for x, y, w, h in faces:
        # frame[y:y+h, x:x+w] = cv2.resize(head, dsize=(w, h))
        cv2.rectangle(frame, pt1=(x,y), pt2=(x+w,y+h), color=[0,0,255], thickness=2)
    cv2.imshow('frame', frame)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
v.release()  # 释放视频流

