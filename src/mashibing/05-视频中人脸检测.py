# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: 05-视频中人脸检测.py
@time: 2023/3/16 17:16
"""

import cv2

# 一秒多少帧，默认25帧
v = cv2.VideoCapture(r'./attachment/ttnk.mp4')
fps = v.get(propId=cv2.CAP_PROP_FPS)
h_ = v.get(propId=cv2.CAP_PROP_FRAME_HEIGHT)
w_ = v.get(propId=cv2.CAP_PROP_FRAME_WIDTH)

face_detector = cv2.CascadeClassifier(r'./attachment/haarcascade_frontalface_alt.xml')
while True:
    flag, frame = v.read()
    # 最后一张图片后面，没有图片，无法读取图片，返回False
    if not flag:
        break

    frame = cv2.resize(frame, dsize=(int(w_//2), int(h_//2)))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 播放慢了，检测人脸耗时操作，扫描整张图片，图片大，耗时长
    faces = face_detector.detectMultiScale2(gray, scaleFactor=1.1, minNeighbors=2)
    for x, y, w, h in faces[0]:
        cv2.rectangle(frame, pt1=(x, y), pt2=(x+w, y+h), color=[0, 0, 255], thickness=2)
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1000 // int(fps))
    if key == ord('q'):
        break

cv2.destroyAllWindows()
v.release()  # 释放视频流