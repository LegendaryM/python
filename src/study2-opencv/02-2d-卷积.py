#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" TODO """

__author__ = 'miracle'

import cv2
import numpy as np

img = cv2.imread('./attachment/opencv-logo.webp')

kernel = np.ones((5,5), dtype=np.float32)/25
# filter2D 可以对一幅图像进行卷积操作
dst = cv2.filter2D(img, -1, kernel)

cv2.imshow('kernel', dst)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
