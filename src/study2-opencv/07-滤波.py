#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" TODO """

__author__ = 'miracle'

from skimage import data
import numpy as np
from matplotlib import pyplot as plt
import cv2


if __name__ == '__main__':
    # 加载图片，处理
    # img = cv2.imread('./attachment/moon.png', flags=cv2.IMREAD_GRAYSCALE)
    img = cv2.imread('./attachment/meigui.jpg', flags=cv2.IMREAD_GRAYSCALE)
    # h, w = img.shape
    # img = cv2.resize(img, dsize=(w // 3, h // 3))
    img2 = img/255  # unit8 -> float32数据

    # 傅里叶变换，移动，将低频移动到中心
    dft = cv2.dft(img2, flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    # 低通滤波：过滤高频波
    # h, w = img.shape
    # h2, w2 = h // 2, w // 2  # 中心点
    # mask = np.zeros((h, w, 2), dtype=np.uint8)
    # mask[h2-50:h2+50,w2-50:w2+50]=1 # 中心区域100*100不变，其他（高频）变成0，高频过滤，噪声
    # dft_shift*= mask

    # 高通滤波: 过滤低频波，保留高频波
    h, w = img.shape
    h2, w2 = h // 2, w // 2  # 中心点
    dft_shift[h2 - 50:h2 + 50, w2 - 50:w2 + 50] = 0
    dft_shift2 = dft_shift

    # 翻转
    ifft_shift = np.fft.ifftshift(dft_shift2)
    result = cv2.idft(ifft_shift)

    # 显示图片
    plt.figure(figsize=(12,12))
    plt.subplot(121)
    plt.imshow(img, cmap='gray')
    plt.subplot(122)
    plt.imshow(result[:,:,0], cmap='gray')
    plt.show()
