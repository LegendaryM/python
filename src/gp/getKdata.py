# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: getKdata.py
@time: 2024/10/16 10:41
说明： 从东方财富网拉数据，暂时不知道并发，做为财经网，并发应该很高
当天：
GET https://webquotepic.eastmoney.com/GetPic.aspx?imageType=r&type=&token=44c9d251add88e27b65ed86506f6e5da&nid=1.600611&timespan=1729046190

K:
GET https://webquoteklinepic.eastmoney.com/GetPic.aspx?nid=0.000550&type=&unitWidth=-6&ef=&formula=MACD&AT=1&imageType=KXL&timespan=1729046102
GET https://webquoteklinepic.eastmoney.com/GetPic.aspx?nid=1.600611&type=&unitWidth=-6&ef=&formula=MACD&AT=1&imageType=KXL&timespan=1729046050

详细信息：


nid: 600沪 -> 1.code
     000深 -> 0.code
"""

from util.my_utils import http_get_req_origin
from util.obs_client import upload_to_obs
import time
import os
from gp.gp_code import all_codes

k_url_base = 'https://webquoteklinepic.eastmoney.com/GetPic.aspx'

img_path = r'E:\temp\4'

def download_upload():
    for tag, codes in all_codes.items():
        length = len(codes)
        for i in range(length):
            code = codes[i]
            png_file = os.path.join(img_path, code + '.png')
            if os.path.exists(png_file):
                print("[%s %s/%s] %s exists, skip" % (tag, i+1, length, code))
                continue
            resp = http_get_req_origin('%s?nid=%s.%s&type=&unitWidth=-6&ef=&formula=MACD&AT=1&imageType=KXL&timespan=%d' % (k_url_base,tag,code, time.time()))
            if resp.status_code != 200:
                print("[%s %s/%s] %s get failed" % (tag, i+1, length, code))

            with open(png_file, 'wb') as f:
                f.write(resp.content)
            print("[%s %s/%s] %s get success: %s" % (tag, i+1, length, code, png_file))
            # time.sleep(0.5)

    print('All download success, start upload to obs.')
    for f in os.listdir(img_path):
        upload_to_obs(os.path.join(img_path, f), r'vpp/1batchSynth/test/k/' + f)
    print('Upload to obs success.')


def clean():
    for f in os.listdir(img_path):
        os.remove(os.path.join(img_path, f))
    print("%s clean success" % img_path)
