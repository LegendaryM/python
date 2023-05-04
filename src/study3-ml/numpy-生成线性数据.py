# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: numpy-生成线性数据.py
@time: 2023/3/24 10:24
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    x = np.random.uniform(-100, 100, (100, ))
    print(x)

    c = np.random.uniform(-300, 300, (100,))
    y = 10 * x + c

    df = pd.DataFrame({'x': x, 'y': y})
    df.to_csv('liner.csv')
    plt.scatter(x, y)
    plt.show()
