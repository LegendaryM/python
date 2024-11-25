# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: test.py
@time: 2024/10/16 10:56
"""

import cv2
from PIL import Image, ImageFilter

image = Image.open(r'E:\temp\4\000001.png')

# 设置压缩参数
compression_level = 9  # 压缩级别，范围为0-9，数值越大，压缩率越高，但文件大小也越大
# filter_type = Image.LANCZOS  # 使用Lanczos滤波器进行重采样，以获得更好的图像质量
image = image.filter(ImageFilter.SMOOTH)
# 保存压缩后的图片
image.save(r'E:\temp\4\000001__.png', "PNG", compress_level=compression_level, optimize=True)