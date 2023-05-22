#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" TODO """

__author__ = 'miracle'


from moviepy.editor import AudioFileClip
import os
video_path = r'C:\Users\miracle_j\Downloads\aisiji_01.mp4'

my_audio_clip = AudioFileClip(video_path)
my_audio_clip.write_audiofile(os.path.splitext(video_path)[0] + '.wav')
