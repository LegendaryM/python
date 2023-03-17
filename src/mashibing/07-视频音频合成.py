# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: 07-视频音频合成.py
@time: 2023/3/17 15:05
"""

from scipy.io import wavfile
import subprocess

# 尽量选择单声道音频, 将双声道转单声道 命令：ffmpeg -i sucai.wav -ac 1 sucai2.wav
samplerate, wav = wavfile.read(r'./attachment/sucai2.wav')
part = wav[10 * samplerate: 13 * samplerate]
wavfile.write(r'./attachment/part.wav', samplerate, part)

cmd = "ffmpeg -i ./attachment/gray.mp4 -i ./attachment/part.wav ./attachment/gray2.mp4"
result = subprocess.call(cmd, shell=True)
print(result)


