# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: 3乘3像素图片.py
@time: 2023/9/4 18:07
"""
import matplotlib.pyplot as plt


def plot_image(image):
    fig = plt.gcf()
    fig.set_size_inches(3, 3)
    plt.imshow(image, cmap='binary')
    plt.show()


Tensor = [
    [[0, 0, 0], [255, 255, 255], [255, 255, 255]],
    [[255, 255, 255], [0, 0, 0], [255, 255, 255]],
    [[255, 255, 255], [255, 255, 255], [0, 0, 0]]
]

plot_image(Tensor)
