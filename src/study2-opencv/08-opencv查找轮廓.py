#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" TODO """

__author__ = 'miracle'

import cv2
import numpy as np


if __name__ == '__main__':
    img = cv2.imread('./attachment/liu.jpg')
    gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)

    # 二值化, 黑白
    threshold, binary = cv2.threshold(gray, 50, 255, cv2.THRESH_OTSU)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    areas = []
    for contour in contours:
        areas.append(cv2.contourArea(contour))
    areas = np.asarray(areas)
    index = areas.argsort()   # 从小到大，倒数第二个，第二大轮廓
    mask = np.zeros_like(gray, dtype=np.uint8)  # mask面具, 纯黑色
    # 纯黑的图片中绘制了白色轮廓
    mask = cv2.drawContours(mask, contours, index[-2], (255, 255, 255), thickness=1)

    cv2.imshow('mask', mask)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()











