# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: 手写数字识别_tensorflow.py
@time: 2023/9/4 14:42
"""

# TODO　未成功
import tensorflow as tf
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
print("Num CPUs Available: ", len(tf.config.experimental.list_physical_devices('CPU')))
# data = mnist.load_data()
(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential(
    [tf.keras.layers.Flatten(input_shape=(28, 28)),
     tf.keras.layers.Dense(128, activation='relu'),
     tf.keras.layers.Dropout(0.2),
     tf.keras.layers.Dense(10, activation='softmax')])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# tf.keras.utils.plot_model(model, to_file='手写数字识别.png', show_shapes=True)
model.fit(x_train, y_train, epochs=10)
model.evaluate(x_test, y_test)
