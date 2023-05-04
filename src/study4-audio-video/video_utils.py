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
        """
        获取视频信息： by cv2
        :return:
        """
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
                         'framecount': total_frames, 'duration': f'{duration:.3f}s'}
        return message_vedio

    def split_audio(self, audio_output_file):
        """
        提取视频中的音频: by moviepy
        :param audio_output_file:
        :return:
        """
        from moviepy.editor import AudioFileClip
        AudioFileClip(self.video_file).write_audiofile(audio_output_file)


if __name__ == '__main__':
    vu = VideoUtils(r'D:\tmp\va\ttnk.mp4')
    print(vu.split_audio(r'D:\tmp\va\ttnk.wav'))