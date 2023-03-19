#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" TODO """

__author__ = 'miracle'

import cv2

img = cv2.imread('./attachment/meigui.jpg')
img = cv2.resize(img,dsize=(img.shape[1]//2, img.shape[0]//2))
canny = cv2.Canny(img, 75, 100)  # 画轮廓边界

cv2.imshow('img', img)
cv2.imshow('canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

