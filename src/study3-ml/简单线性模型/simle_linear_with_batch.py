# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: simple_logical_model.py
@time: 2023/5/16 16:28
"""

import numpy as np
from matplotlib import pyplot as plt
import matplotlib
import math

zhfont1 = matplotlib.font_manager.FontProperties(fname="SourceHanSansSC-Bold.otf")

x_y = np.loadtxt(r'./input_output_linear.csv', delimiter=',')
x, y = x_y[0:2], x_y[3]
# print(x_y.shape)
# plt.title('y=2x+0.3')
# plt.xlabel('自变量x', fontproperties=zhfont1)
# plt.ylabel('因变量y', fontproperties=zhfont1)
# plt.plot(x_y[0], x_y[1])
# plt.show()

# y = wx + b
w = np.random.rand(1)
b = np.random.rand(1)
lr = np.random.rand(1)
m = len(x_y)
print('init w,b,lr', w, b, lr)
batch_size = 10  # mini batch
batch_num = math.ceil(len(x_y) / batch_size)
# 最优参数
mini_cost = 10
mini_w = 10
mini_b = 10
mini_epoch = -1

for epoch in range(0, 2000):
    cost = 0

    for i in range(0, batch_num):
        start_index = i * batch_size
        end_index = (i + 1) * batch_size
        if end_index > len(x_y):
            end_index = len(x_y)

        y_hat = w * x_y[start_index:end_index, 0] + b
        cost = np.sum(np.square(y_hat - x_y[start_index:end_index, 1]))
        dw = 1/m * np.sum((y_hat - x_y[start_index:end_index, 1]) * x_y[start_index:end_index, 0])
        w = w - lr * dw

        db = 1/m * np.sum(y_hat - x_y[start_index:end_index, 1])
        b = b - lr * db
        cost += cost * 1 / (2 * m)

    if cost < mini_cost:
        mini_cost = cost
        mini_w = w
        mini_b = b
        mini_epoch = epoch

    print(epoch, 'cost:', cost, ' w:', w, ' b:', b)

print('final mini_epoch', mini_epoch, 'mini_cost:', mini_cost, 'mini_w:', w, 'mini_b:', b)



