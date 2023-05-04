# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: video_utils.py
@time: 2023/5/4 18:03
"""

import cv2
import os


class VideoUtils(object):

    def __init__(self, video_file):
        self.video_file = video_file

    def get_video_info(self):
        cap = cv2.VideoCapture(self.video_file)
        if not cap.isOpened():
            return 0
        # 获取视频基本信息
        fileSize = os.path.getsize(self.video_file) / (2 ** 20)  # 单位Mib
        fps = int(cap.get(cv2.CAP_PROP_FPS))  # 帧率
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 宽度
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 高度
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 总图像帧数
        duration = total_frames / fps
        message_vedio = {'m_size': f"{fileSize:.4f} Mib", 'fps': fps, 'w': width, 'h': height,
                         'framecount': total_frames, 'duration': duration}
        return message_vedio


if __name__ == '__main__':
    vu = VideoUtils(r'C:\Users\Administrator\Desktop\temp\test.mp4')
    print(vu.get_video_info())