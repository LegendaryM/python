#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" TODO """

__author__ = 'miracle'


from moviepy.editor import VideoFileClip,concatenate_videoclips

import os

save_path = r"E:\temp/合并结果.mp4"  # 合并后的视频名称

# 开始合并
file_names = []

ts_files = os.listdir(r'E:\temp\ts_de')
ts_files.sort(key=lambda x:int(x[:-3]))
for ts_file in ts_files:
    # 载入视频
    video = VideoFileClip(os.path.join(r'E:\temp\ts_de', ts_file))
    # 添加到数组
    file_names.append(video)
    print(os.path.join(r'E:\temp\ts_de', ts_file), " ok")

# 拼接视频
clip = concatenate_videoclips(file_names)

# 生成目标视频文件
clip.to_videofile(save_path, fps=25, remove_temp=False)