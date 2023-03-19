#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" TODO """

__author__ = 'miracle'


import numpy as np
import cv2
import matplotlib.pyplot as plt


if __name__ == '__main__':
    moon = cv2.imread('./attachment/moon.png')
    # 快速傅里叶变换  时域 -> 频域
    fft_ = np.fft.fft2(moon)

    # f_abs = np.abs(fft_)
    # print(f_abs.mean())  # 噪声
    # print(np.median(f_abs))  # 中值
    # print(f_abs.min())
    # print(np.quantile(f_abs, [0.25, 0.5, 0.75, 0.9]))   # 几等分方法
    # f_abs2 = np.where(f_abs > 88, 0, f_abs)    #高通滤波，高频过滤了
    # moon2 = np.fft.ifft2(f_abs2)
    # moon2 = np.real(moon2)  # 去除虚部，保留实部
    fshift = np.fft.fftshift(fft_)    # 低频数据已到中心
    row, col = moon.shape[0] // 2, moon.shape[1] // 2
    fshift[row-30:row+30, col-30:col+30] = 0
    f = np.fft.ifftshift(fshift)
    moon2 = np.fft.ifft2(f)     # 频域 -> 时域
    moon2 = np.abs(moon2)

    plt.subplot(121)
    plt.imshow(moon, cmap='gray')
    plt.subplot(122)
    plt.imshow(moon2, cmap='gray')
    plt.show()










