# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: test.py
@time: 2023/3/16 16:01
"""

import cv2
import numpy as np

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 100, (255, 0,0), 1)


img = np.zeros((1024, 960, 3), dtype=np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)
    key = cv2.waitKey(2000)
    if key == ord('q'):
        break
cv2.destroyAllWindows()

