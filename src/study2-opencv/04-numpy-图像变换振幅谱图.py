#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" TODO """

__author__ = 'miracle'

from skimage import data
import numpy as np
from matplotlib import pyplot as plt


if __name__ == '__main__':
    moon = data.moon()
    # 时域到频域
    f = np.fft.fft2(moon)
    fftshift = np.fft.fftshift(f)
    magnitude_spectrum = 20 * np.log(np.abs(fftshift))

    # 振幅谱图
    # 121 一行两列第一个 122:一行两列第二个
    plt.subplot(121)
    plt.imshow(moon, cmap='gray')
    plt.title('moon')
    plt.subplot(122)
    plt.imshow(magnitude_spectrum)
    plt.title('Magitude Spectrum')
    plt.show()
