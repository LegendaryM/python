# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: 搭建本地web.py
@time: 2023/9/12 11:21
"""

import cv2
import torch
import torch.nn as nn

m = nn.Linear(20, 30)
input = torch.randn(128, 20)
output = m(input)
print(output.size())
print(m)
