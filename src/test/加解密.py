#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" TODO """

__author__ = 'miracle'

from Crypto.Cipher import AES


def get_aes_from_keyfile(key_file):
    with open(key_file, "rb") as k:
        password = k.read()
    return AES.new(password, AES.MODE_CBC, iv=password)  # 创建一个aes对象


def decrypt(aes, input_file, output_file) :
    with open(input_file, "rb") as input:
        file_input_b = input.read()

    output = aes.decrypt(file_input_b)
    with open(output_file, 'wb') as f:
        f.write(output)
        f.close()
    print('input:', input_file, " => output:", output_file, " success")


aes = get_aes_from_keyfile(r'E:\temp\enc.key')
import os
ts_files = os.listdir(r'E:\temp\ts')
for ts_file in ts_files:
    if os.path.exists(os.path.join(r'E:\temp\ts_de', ts_file)):
        continue
    decrypt(aes, os.path.join(r'E:\temp\ts', ts_file), os.path.join(r'E:\temp\ts_de', ts_file))