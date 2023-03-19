#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" TODO """

__author__ = 'miracle'

from skimage import data
import numpy as np
from matplotlib import pyplot as plt
import cv2


if __name__ == '__main__':
    moon = data.moon()
    # 时域到频域
    dft = cv2.dft(np.float32(moon), flags=cv2.DFT_COMPLEX_OUTPUT)
    fftshift = np.fft.fftshift(dft)

    magnitude_spectrum = 20 * np.log(cv2.magnitude(fftshift[:,:,0], fftshift[:,:,1]))

    # 振幅谱图
    # 121 一行两列第一个 122:一行两列第二个
    plt.subplot(121)
    plt.imshow(moon, cmap='gray')
    plt.title('moon')
    plt.subplot(122)
    plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Magitude Spectrum')
    plt.show()
