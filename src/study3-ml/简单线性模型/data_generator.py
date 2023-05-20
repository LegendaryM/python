# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: data_generator.py
@time: 2023/5/17 17:10
"""
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

# 单个特征
x = np.random.rand(500).reshape((500, 1))
b = np.random.rand(500)
y = 2 * x + 0.3
# print(x)
# print('--------------------------------')
# print(y)

x_y = np.concatenate((x,y), axis=1)
print(x_y)
np.savetxt("input_output_linear.csv", x_y, delimiter=",")


