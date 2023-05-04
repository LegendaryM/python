# -*- coding: utf-8 -*-

"""

@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: audio_utils.py
@time: 2023/5/4 16:58
"""

import librosa  # 只会导入librosa.__init__.py信息，而不会导入下级文件中的信息，使用子目录时，需要手动导入子目录，例如librosa.feature
import librosa.feature
from sklearn import preprocessing
import matplotlib.pyplot as plt
import soundfile as sf

"""
    参考： https://www.jianshu.com/p/8d6ffe6e10b9
    sr：采样率
    hop_length：帧移
    overlapping：连续帧之间的重叠部分
    n_fft：窗口大小
    spectrum：频谱
    spectrogram：频谱图或叫做语谱图
    amplitude：振幅
    mono：单声道、stereo：立体声
"""
class AudioUtils(object):
    def __init__(self, audio_file):
        self.audio_file = audio_file
        self.audio_sf = sf.SoundFile(self.audio_file)
        self.sr = self.audio_sf.samplerate
        self.mono = self.audio_sf.channels == 1
        self.duration = self.audio_sf.frames / self.sr
        self.frame_data, _ = librosa.load(self.audio_sf, sr=self.sr, mono=self.mono)

    def get_audio_info(self):
        """
        获取音频信息： samplerate、channel、frame、subtype、duration
        :param audio_file:
        :return:
        """
        audio_info = {'sr': self.audio_sf.samplerate, 'channel': ('mono' if self.mono else 'stereo'),
                      'frame(num of samples)': self.audio_sf.frames,
                      'subtype': self.audio_sf.subtype,
                      'duration': f'{self.duration:.3f} s'}
        return audio_info

    def get_audio_clip(self, start_sec, end_sec, output_file=None):
        """
        获取音频片段
        :param start_sec: 秒
        :param end_sec: 秒
        :param output_file:
        :return:
        """
        if end_sec >= self.duration:
            audio_clip = self.frame_data
        else:
            audio_clip = self.frame_data[..., start_sec*self.sr: end_sec*self.sr]

        if output_file:
            sf.write(output_file, audio_clip.T, self.sr, format='wav')
        else:
            return audio_clip

    def make_wave_diagram(self):
        """
        绘制波形图
        :return:
        """
        plt.figure(figsize=(20, 5))
        librosa.display.waveshow(self.frame_data, sr=self.sr)
        plt.show()

    def make_spectorgram(self):
        """
        绘制频谱图： 声音频率随时间变化的频谱的可视化
        :return:
        """
        stft = librosa.stft(self.frame_data)
        db = librosa.amplitude_to_db(abs(stft))
        plt.figure(figsize=(20, 5))
        librosa.display.specshow(db, sr=self.sr, x_axis='time', y_axis='hz')
        plt.colorbar()
        plt.show()

    def make_mfcc(self):
        """
        梅尔频率倒谱系数 (MFCC) 是一小组特征（通常约为 10-20），它们简明地描述了频谱包络的整体形状。
        在 MIR 中，它经常被用来描述音色。
        :return:
        """
        mfccs = librosa.feature.mfcc(y=self.frame_data, sr=self.sr)
        plt.figure(figsize=(20, 5))
        librosa.display.specshow(mfccs, sr=self.sr, x_axis='time')
        plt.colorbar()
        plt.show()

    def make_zcr(self):
        """
        过零率（zero-crossing rate，ZCR）是指一个信号的符号变化的比率，例如信号从正数变成负数，或反过来
        :return:
        """
        zcrs = librosa.feature.zero_crossing_rate(self.frame_data)
        print(zcrs.shape)
        plt.figure(figsize=(14, 5))
        plt.plot(zcrs[0])
        plt.show()

    def make_spectral_centroid(self):
        """
        频谱质心（维基百科）表示频谱能量集中在哪个频率上。这就像一个加权平均值：
        :return:
        """
        spectral_centroids = librosa.feature.spectral_centroid(y=self.frame_data, sr=self.sr)[0]

        frames = range(len(spectral_centroids))
        t = librosa.frames_to_time(frames)

        librosa.display.waveshow(self.frame_data, sr=self.sr, alpha=0.4)
        plt.plot(t, self.normalize(spectral_centroids), color='r')
        plt.show()

    def normalize(self, x, axis=0):
        return preprocessing.minmax_scale(x, axis=axis)

    def make_spectral_bandwidth(self):
        """
        频谱带宽: 用来计算p-order频谱带宽
        :return:
        """
        spectral_centroids = librosa.feature.spectral_centroid(y=self.frame_data, sr=self.sr)[0]

        frames = range(len(spectral_centroids))
        t = librosa.frames_to_time(frames)

        spectral_bandwidth_2 = librosa.feature.spectral_bandwidth(y=self.frame_data + 0.01, sr=self.sr)[0]
        spectral_bandwidth_3 = librosa.feature.spectral_bandwidth(y=self.frame_data + 0.01, sr=self.sr, p=3)[0]
        spectral_bandwidth_4 = librosa.feature.spectral_bandwidth(y=self.frame_data + 0.01, sr=self.sr, p=4)[0]
        librosa.display.waveshow(self.frame_data, sr=self.sr, alpha=0.4)
        plt.plot(t, self.normalize(spectral_bandwidth_2), color='r')
        plt.plot(t, self.normalize(spectral_bandwidth_3), color='g')
        plt.plot(t, self.normalize(spectral_bandwidth_4), color='y')
        plt.legend(('p = 2', 'p = 3', 'p = 4'))
        plt.show()

    def make_spectral_rolloff(self):
        """
        频谱滚降/频谱衰减：总频谱能量的特定百分比所在的频率。
        :return:
        """
        spectral_centroids = librosa.feature.spectral_centroid(y=self.frame_data, sr=self.sr)[0]

        frames = range(len(spectral_centroids))
        t = librosa.frames_to_time(frames)

        spectral_rolloff = librosa.feature.spectral_rolloff(y=self.frame_data + 0.01, sr=self.sr)[0]
        librosa.display.waveshow(self.frame_data, sr=self.sr, alpha=0.4)
        plt.plot(t, self.normalize(spectral_rolloff), color='r')
        plt.show()

    def make_chroma_feature(self):
        """
        色度特征：是一个典型的 12 元素特征向量，指示每个音高类别{C, C#, D, D#, E, ..., B}的能量是多少存在于信号中。
        :return:
        """
        chromagram = librosa.feature.chroma_stft(y=self.frame_data, sr=self.sr, hop_length=512)
        plt.figure(figsize=(15, 5))
        librosa.display.specshow(chromagram, x_axis='time', y_axis='chroma', hop_length=512, cmap='coolwarm')
        plt.show()


if __name__ == '__main__':
    au = AudioUtils(r'D:\tmp\va\ttnk_clip.wav')
    # au = AudioUtils(r'D:\tmp\va\ttnk.wav')
    print(au.get_audio_info())
    # print(au2.make_wave_diagram())
    print(au.get_audio_clip(10,30,r'D:\tmp\va\ttnk_clip_2.wav'))
