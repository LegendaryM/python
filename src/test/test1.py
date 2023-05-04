#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import torch
import

img1 = cv2.imread(r'./liu.jpg')
img1 = cv2.cvtColor(img1, code=cv2.COLOR_BGR2GRAY)
# print(img1)

test_img = []
for i in range(0, 480):
    single = []
    for j in  range(0, 540):
        if j < 540//2:
            single.append(254)
        else:
            single.append(0)
    test_img.append(single)
kernal = [[1,0,-1],[1,0,-1],[1,0,-1]]
kernal = np.array(kernal, dtype=np.int8)
img = np.array(test_img, dtype=np.uint8)

result = np.convolve(img, kernal)
# print(img)
cv2.imshow('test', result)
cv2.waitKey(0)
cv2.destroyAllWindows()















