# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: 09-opencv腐蚀与膨胀.py
@time: 2023/3/20 10:02
"""

import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('./attachment/fushi.jpg')
    # 指定全为1的3*3矩阵，卷积计算后，该像素点的值等于以该像素点为中心的3*3范围内的最大值
    # 由于图像是二值图像，只要包含周围白的部分，就变为白的
    kernel = np.ones((3, 3), dtype=np.uint8)
    # 膨胀：用来处理缺陷问题，会将图片白色部分膨胀，消除边缘的缺陷问题
    dilate = cv2.dilate(img, kernel,
                        iterations=2)   # 迭代次数：将对图片进行2次膨胀
    # 腐蚀：用来消除毛刺问题, 腐蚀与膨胀操作相反。
    # 取图像中3*3区域内的最小值，也就是取0（黑色），只要原图片3*3范围内有黑的，该像素点就是黑的
    erode = cv2.erode(img, kernel, iterations=2)

    cv2.imshow('raw', img)
    cv2.imshow('dilate', dilate)
    cv2.imshow('erode', erode)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

