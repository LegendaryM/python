# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: 语音合成.py
@time: 2023/5/22 10:25
"""

import http.client
import urllib.parse
import json
from ai_ability.config import *

def processGETRequest(appKey, token, text, audioSaveFile, format, sampleRate) :
    host = 'nls-gateway-cn-shanghai.aliyuncs.com'
    url = 'https://' + host + '/stream/v1/tts'
    # 设置URL请求参数
    url = url + '?appkey=' + appKey
    url = url + '&token=' + token
    url = url + '&text=' + text
    url = url + '&format=' + format
    url = url + '&sample_rate=' + str(sampleRate)
    # voice 发音人，可选，默认是xiaoyun。
    # url = url + '&voice=' + 'xiaoyun'
    # volume 音量，范围是0~100，可选，默认50。
    # url = url + '&volume=' + str(50)
    # speech_rate 语速，范围是-500~500，可选，默认是0。
    # url = url + '&speech_rate=' + str(0)
    # pitch_rate 语调，范围是-500~500，可选，默认是0。
    # url = url + '&pitch_rate=' + str(0)
    print(url)
    # Python 2.x请使用httplib。
    # conn = httplib.HTTPSConnection(host)
    # Python 3.x请使用http.client。
    conn = http.client.HTTPSConnection(host)
    conn.request(method='GET', url=url)
    # 处理服务端返回的响应。
    response = conn.getresponse()
    print('Response status and response reason:')
    print(response.status ,response.reason)
    contentType = response.getheader('Content-Type')
    print(contentType)
    body = response.read()
    if 'audio/mpeg' == contentType :
        with open(audioSaveFile, mode='wb') as f:
            f.write(body)
        print('The GET request succeed!')
    else :
        print('The GET request failed: ' + str(body))
    conn.close()
def processPOSTRequest(appKey, token, text, voice_map) :
    host = 'nls-gateway-cn-shanghai.aliyuncs.com'
    url = 'https://' + host + '/stream/v1/tts'
    # 设置HTTPS Headers。
    httpHeaders = {
        'Content-Type': 'application/json'
        }
    # 设置HTTPS Body。
    body = {'appkey': appKey, 'token': token, 'text': text, **voice_map}
    body = json.dumps(body)
    # print('The POST request body content: ' + body)
    conn = http.client.HTTPSConnection(host)
    conn.request(method='POST', url=url, body=body, headers=httpHeaders)
    # 处理服务端返回的响应。
    response = conn.getresponse()
    print('Response status and response reason:')
    print(response.status ,response.reason)
    contentType = response.getheader('Content-Type')
    print(contentType)
    body = response.read()
    if 'audio/mpeg' == contentType :
        with open(voice_map['audioSaveFile'], mode='wb' if voice_map['is_first'] else 'ab+') as f:
            f.write(body)
        print('The POST request succeed!')
    else :
        print('The POST request failed: ' + str(body))
    conn.close()


def split_sentence_with_300(text: str):
    if len(text) <= 300:
        return [text]

    texts = []
    temp = 0
    start_index = 0
    while True:
        index = text.find('。', temp)
        if index == -1:
            texts.append(text[start_index:temp])
            break
        if index - start_index < 300:
            temp = index + 1
        else:
            texts.append(text[start_index:temp])
            start_index = temp
    return texts


import wave

def pcm2wav(pcm_file, wav_file, channels=1, bits=16, sample_rate=16000):
    pcmf = open(pcm_file, 'rb')
    pcmdata = pcmf.read()
    pcmf.close()

    if bits % 8 != 0:
        raise ValueError("bits % 8 must == 0. now bits:" + str(bits))

    wavfile = wave.open(wav_file, 'wb')
    wavfile.setnchannels(channels)
    wavfile.setsampwidth(bits // 8)
    wavfile.setframerate(sample_rate)
    wavfile.writeframes(pcmdata)
    wavfile.close()

appKey = ali_ak
token = 'd8ffff64c1a94773b11bcf4c0570cf5e'
text = '简单哥说简单电影。黑心老板，为了得到竞争对手的秘密，派遣女秘引诱对方。在激情时刻，给对方致命一击，然而他们都小看了对方。人都有秘密，猛兽师桑尼，已经连赢了十几场比赛，所有人都不知道她连胜的原因，她甚至连队友都未曾告知过，直到她被人杀死，秘密逐渐浮现。原来斗兽才是她的本体。她的每一次战斗失败，就意味着死亡。'
texts = split_sentence_with_300(text)

# 超过300时，分段合成后拼接
audio_save_file = 'result.pcm'
for text, index in zip(texts, range(len(texts))):
    # 采用RFC 3986规范进行urlencode编码。
    textUrlencode = text
    textUrlencode = urllib.parse.quote_plus(textUrlencode)
    textUrlencode = textUrlencode.replace("+", "%20")
    textUrlencode = textUrlencode.replace("*", "%2A")
    textUrlencode = textUrlencode.replace("%7E", "~")

    voice_map = {
        'voice': 'zhitian_emo',          # 声音支持： https://help.aliyun.com/document_detail/84435.htm?spm=a2c4g.94737.0.0.367e38adHhIqRP#topic-2572243
        'volume': 50,                    # 音量，取值范围：0~100，默认值：50。
        'speech_rate': 0,                # 语速，取值范围：-500~500，默认值：0
        'pitch_rate': 0,                  # 语调，取值范围：-500~500，默认值：0。
        'audioSaveFile': audio_save_file,
        'format': 'pcm',
        'sampleRate': 16000
    }

    is_first = True
    if index > 0:
        is_first = False

    voice_map['is_first'] = is_first
    # POST请求方式
    processPOSTRequest(appKey, token, text, voice_map)

pcm2wav('result.pcm', 'result.wav')