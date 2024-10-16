#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" TODO """

__author__ = 'miracle'


import os

save_path = r"E:\temp/合并结果.mp4"  # 合并后的视频名称

# 开始合并
file_names = []

ts_files = os.listdir(r'E:\temp\ts_de')
ts_files.sort(key=lambda x:int(x[:-3]))
# ts_files = ['0.ts', '1.ts']
file_bytes = []
for ts_file in ts_files:
    with open(os.path.join(r'E:\temp\ts_de', ts_file), 'rb') as f:
        file_bytes.extend(f.read())

with open(save_path, 'wb') as s:
    s.write(bytes(file_bytes))
    s.close()