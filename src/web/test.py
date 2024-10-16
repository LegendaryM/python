# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: test.py
@time: 2024/2/20 14:43
"""


import os
import subprocess

def get_ffmpeg_info(file):
    cmd_p = subprocess.Popen('ffmpeg -i %s -hide_banner' % file, shell=True, stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cmd_result = ""
    for i in cmd_p.stdout.readlines():
        cmd_result += i.decode()
    for i in cmd_p.stderr.readlines():
        cmd_result += i.decode()
    return cmd_result

path = r'C:\Windows\Path1'
idx = 30
for i in os.listdir(path):
    # os.rename(os.path.join(path, i), '%s/%s' % (path, idx))
    # print(i)
    # idx += 1
    v_path = os.path.join(path, i)
    info = get_ffmpeg_info(v_path)
    if "mpegts" in info:
        v_path_new = os.path.join(path, "%s.mp4" % i)
        os.system("ffmpeg -i %s -c:v libx264 -crf 19 -y %s" % (v_path, v_path_new))
    else:
        print("skip", v_path)



