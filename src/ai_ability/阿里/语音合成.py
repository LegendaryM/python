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
token = '21e05eec4bde4bf4876e39b5d54ba010'
text = '桑尼是一个用脑电波与斗兽连接意识的驯兽师，他所控制的斗兽已经连续赢了十七场比赛。一个大佬想用重金买通桑尼，让故意输一场，但被拒绝了。从队友口中得知，桑尼曾被人绑架，或许从前的遭遇给了他复仇的力量。比赛场面异常激烈，对方的驯兽师几次跳起来怒吼，而桑尼却纹丝不动，在最后一刻反败为胜，赢了比赛。桑尼在后台偶遇大佬身边的白莲花，他很好奇桑尼的优势是什么，利于桑尼一步一步走近他，趁其不备，给了桑尼致命一击，但此刻才发现，桑尼只是一副人类的躯壳。而原来真正的桑尼在那次绑架中头部伤势严重，他把意识转移到了斗兽体。所以别人格斗时是用人的意识操纵斗兽，而他却正好相反，斗兽才是他的本体，他是用自己的真身在战斗，一旦失败，就意味着死亡。献出真挚的桑尼自然不会放过大佬。不过他最后说出了秘密，桑尼的优势不是复仇，而是恐惧。每次进入竞技场，我都在为我的生命而战斗。'
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