# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: data_generator.py.py
@time: 2023/4/27 22:51
"""


import torch
import numpy as np

# 3个特征
n = 500
n_x = 3
x = np.random.rand(n_x * n).reshape((n, n_x))
y = np.where(np.abs(np.random.rand(n).reshape((n,1))) > 0.5, 1, 0)
print(x.shape, y.shape)

# print(x)
# print('--------------------------------')
# print(y)

x_y = np.concatenate((x,y), axis=1)
print(x_y)
np.savetxt("input_output_logical.csv", x_y, delimiter=",")
