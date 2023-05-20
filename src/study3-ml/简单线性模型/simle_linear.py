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
x, y = x_y[0], x_y[1]
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
# 最优参数
mini_cost = 10
mini_w = 10
mini_b = 10
mini_epoch = -1

# 简单线性模型： y = wx + b
for epoch in range(0, 200):
    cost = 0

    for i in x_y:
        y_hat = w * i[0] + b
        cost = np.sum(np.square(y_hat - i[1]))
        dw = (y_hat - i[1]) * i[0]
        w = w - lr * dw

        db = (y_hat - i[1])
        b = b - lr * db
        cost += cost * 1 / (2 * m)

    print(epoch, 'cost:', cost, ' w:', w, ' b:', b)
    if cost < mini_cost:
        mini_cost = cost
        mini_w = w
        mini_b = b
        mini_epoch = epoch

print('final mini_epoch', mini_epoch, 'mini_cost:', mini_cost, 'mini_w:', w, 'mini_b:', b)



