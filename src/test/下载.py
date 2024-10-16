#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
# import torch
# import
import os
from multiprocessing import Queue, Process, Manager
import multiprocessing
import requests
from util.my_utils import download_file

with open(r"E:\temp\index.m3u8", "r", encoding='utf-8') as f:
    data = f.read()
    man_names = data.split('\n')

ts_files = []
for line in man_names:
    if line.startswith("#"):
        continue
    ts_files.append(line)

ts_file_path = r'E:\temp\ts'
for i in range(0, len(ts_files)):
    f = os.path.join(ts_file_path, '%s.ts' % i)
    if os.path.exists(f):
        continue
    for j in range(0,3):
        try:
            download_file('https://vip15.play-cdn15.com/20240202/27086_ff97872b/2000k/hls/' + ts_files[i], os.path.join(ts_file_path, '%s.ts' % i))
            print('%s -> download ok ' % i)
            break
        except Exception as e:
            print("%s -> retry" % i)
            continue

