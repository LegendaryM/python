# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: test.py
@time: 2023/3/16 16:01
"""

import numpy as np

# b = np.repeat([[1, 2]], 2, axis=0)
# print(b)

a = [1, 2, 3]
for i, j in enumerate(a, start=10):
    print(i, j)
