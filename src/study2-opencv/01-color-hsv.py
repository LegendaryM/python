#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" TODO """

__author__ = 'miracle'

import cv2
import numpy as np

if __name__ == '__main__':
    img1 = cv2.imread(r'./attachment/meigui.jpg')
    img1 = cv2.resize(img1, dsize=(img1.shape[1]//2, img1.shape[0]//2))
    img2 = cv2.cvtColor(img1, code=cv2.COLOR_BGR2HSV)
    # print(img2.shape)
    # print('------------', img2[:,:,0].min(), img2[:,:,0].max(),  img2[:,:,1].max(),  img2[:,:,2].max())
    # 定义在HSV颜色空间中红色的范围
    lower_red = np.array([156, 50, 50])
    upper_red = np.array([180, 255, 255])
    # 根据红色的范围，标记图片中哪些位置是红色
    # 如果在，标记为255（白色），否则标记为0（黑色）
    mask = cv2.inRange(img2, lower_red, upper_red)
    # print(mask[:,:].distinct())
    # print(mask[:,:].min())
    res = cv2.bitwise_and(img1, img1, mask=mask)
    cv2.imshow('img1', img1)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
