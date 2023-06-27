# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: my_utils.py
@time: 2023/5/12 14:58
"""
import requests
import json
import time
import soundfile as sf
import os

headers = {"content-type": "application/json"}


def http_post_req(url, json_param, timeout=60):
    """
    http协议的post请求
    :param timeout:
    :param url:
    :param json_param: json参数
    :return:
    """
    return requests.post(url, data=json.dumps(json_param), headers=headers, timeout=timeout).json()


def http_get_req(url, timeout=60, headers=None):
    print('get req:', url)
    """
    http协议的post请求
    :param params:
    :param timeout:
    :param url:
    :param json_param: json参数
    :return:
    """
    return requests.get(url, timeout=timeout, headers=headers).json()

def get_current_time(show_type='ms'):
    """
    获取当前时间
    :param show_type: str s or ms
    :return: 10位 or 13位
    """
    current = time.time()
    if show_type == 's':
        return int(current)
    else:
        return int(round(current * 1000))


def sleep(sleep_second):
    """
    休眠
    :param sleep_second:
    :return:
    """
    time.sleep(sleep_second)


def get_audio_mill_second(audio_file):
    """
    获取音频毫秒数
    :param audio_file:
    :return:
    """
    local_file = audio_file
    if not os.path.exists(audio_file) and audio_file.startswith('http'):
        local_file = os.getenv('TEMP') + audio_file[audio_file.rindex('/') + 1:]
        download_file(audio_file, local_file)
    file = sf.SoundFile(local_file)
    duration = int((file.frames / file.samplerate) * 1000)
    file.close()
    return duration


def download_file(url, local_file):
    # download
    r = requests.get(url)
    with open(local_file, "wb") as f:
        for chunk in r.iter_content(chunk_size=512):
            f.write(chunk)
        f.flush()
    print(url, 'download success')


if __name__ == '__main__':
    import random
    print(random.random)