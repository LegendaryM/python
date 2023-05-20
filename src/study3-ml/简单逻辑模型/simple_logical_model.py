# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: simple_logical_model.py
@time: 2023/5/16 16:28
"""

import numpy as np

x_y = np.loadtxt(r'./input_output_logical.csv', delimiter=',')
x, y = x_y[0:2], x_y[3] # x1, x2, x3

# sigmod和relu函数都不会改变它的维度
# relu函数： a = max(0, z)
def relu(z):
    return np.where(z > 0, z, 0)

# derivative of ReLU
def d_relu(z):
    return np.where(z > 0, 1, 0)

# sigmod function: a = 1/(1+e(-z))
def sigmod(z):
    return 1 / (1 + np.exp(-z))

# m = len(x_y)
# batch_size = 10  # mini batch
# batch_num = math.ceil(len(x_y) / batch_size)

# 逻辑模型 w的特征数跟F_input一致
# layer1: F_input:3, F_output:3, activate: ReLU
# layer2: F_input:3, F_output:2, activate: ReLU
# layer3: F_input:2, F_output:1, activate: sigmod y_hat



# x:(Nf, m) 即行是特征，列是样本，单个样本就是一个列向量。w也是列向量
# 隐藏层的输出：行也是特征，列是样本
# w:(input, output) b:(output, 1) w.T:(output, input) => z:(Nf, m)
# dw是一个列向量，即w.T
w1 = np.random.rand(3 * 3).reshape((3, 3))                   #w1:(3,3)
b1 = np.random.rand(1 * 3).reshape((3, 1))                   #b1:(3,1)

w2 = np.random.rand(3 * 2).reshape((3, 2))                   #w2:(3,2)
b2 = np.random.rand(1 * 2).reshape((2, 1))                   #b2:(2,1)

w3 = np.random.rand(2 * 1).reshape((2, 1))                   #w3:(2,1)
b3 = np.random.rand(1 * 1).reshape((1, 1))                   #b3:(1,1)

lr = np.random.rand(1)
print('init l1:', w1, b1)
print('init l2:', w2, b2)
print('init l3:', w3, b3)
print('init lr:', lr)

# 先从简单得来： with no batch
# 最优参数
mini_cost = 10
mini_epoch = -1

for epoch in range(0, 200):
    loss = 0
    # z和a的第一个维度是样本数， 第二个维度是layer的输出
    for i in x_y:
        # l1: x1w1.T + b2 a1: ReLU(z1)
        x = i[0:3].reshape((-1,1))             # x:(3,1)
        y = i[3]                                # y:(1,1)
        z1 = np.dot(w1.T, x) + b1            # w1.T:(3,3) x:(3,1) => z1(3,1)
        a1 = relu(z1)                           # a1:(3,1)   a1的维度跟z1一致 激活函数不会改变数据的维度，导数也应该不会改变数据的维度

        #l2: a1w2.T + b2 a2: ReLU(z2)
        z2 = np.dot(w2.T, a1) + b2           # w2.T:(2, 3)  => z2:(2,1)
        a2 = relu(z2)                           # a2:(2,1)

        #l3: a2w3.T + b3 a3: ReLU(z3)
        z3 = np.dot(w3.T, a2) + b3           # w3.T:(1,2) => z3:(1,1)
        a3 = sigmod(z3)                         # a3 = y_hat (1,1)
        y_hat = a3[0][0]

        # back propagation
        loss += -(y * np.log(y_hat) + (1-y) * np.log(1-y_hat))
        # dz3 = a3 - y
        dz3 = a3 - i[3]                         # dz3:(1,1)
        dw3 = np.dot(dz3, a2.T)                 # dz3:(1,1) a2.T:(1,2) => dw3:(1, 2)  w3:(2,1)
        db3 = dz3                               # db3:(1,1)
        da2 = np.dot(dz3, w3.T)

        # dz2 = w3.Tdz3 * g'(z2)
        dz2 = np.dot(w3, dz3) * d_relu(z2)           # w3.T:(1,2) dz3:(1,1) g(z2):(2,1) => dz2:(1,1)  element-wise product d2(2,1)???
        dw2 = np.dot(dz2, a1.T)                      # dz2:(2,1) a1.T:(1,3) => dw2:(2, 3)  w2:(3,2)
        db2 = dz2                                       # db2:(2,1)

        # dz1 = dz2 * w2.T * g'(z1)
        dz1 = np.dot(w2, dz2) * d_relu(z1)          # w2.T:(2,3) dz2:(1,1) g(z1):(3,1) => dz1:(2,1)  ?
        dw1 = np.dot(dz1, x.T)                         # dz1:(2,1) x.T:(1,3) => dw1:(2, 3)   w1:(3,3)
        db1 = dz1                               # db1:(2,1)

        # simultaneously update
        w3 = w3 - lr * dw3
        b3 = b3 - lr * db3

        w2 = w2 - lr * dw2
        b2 = b2 - lr * db2

        w1 = w1 - lr * dw1
        b1 = b1 - lr * db1

    loss = loss / len(x_y)
    print(epoch, 'cost:', loss, w3, b3, w2, b2, w1, b1)

    # if loss < mini_cost:
    #     mini_cost = cost
    #     mini_epoch = epoch

print('final cost:', loss, w3, b3, w2, b2, w1, b1)



