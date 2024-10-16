# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: 搭建本地web.py
@time: 2023/3/16 16:01
"""

import numpy as np

t = np.linspace(0,1,1000,endpoint=False)

# x = np.sin(2 * np.pi * 5 * t) + np.sin(2 * np.pi * 10 * t)
x = np.sin(2 * np.pi * 5 * t)
import matplotlib.pyplot as plt
plt.figure()
plt.plot([x for x in range(1000)], np.abs(x))
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')
plt.show()


X = np.fft.fft(x)

freqs = np.fft.fftfreq(len(x), d=t[1] - t[0])

import matplotlib.pyplot as plt
plt.figure()
plt.plot(freqs, np.abs(X))
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')
plt.show()





