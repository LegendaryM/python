# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: getKdata.py
@time: 2024/10/16 10:41
说明： 从东方财富网拉数据，暂时不知道并发，做为财经网，并发应该很高
当天：
GET https://webquotepic.eastmoney.com/GetPic.aspx?imageType=rc&type=&token=44c9d251add88e27b65ed86506f6e5da&nid=1.600611&timespan=1729046190

K:
GET https://webquoteklinepic.eastmoney.com/GetPic.aspx?nid=0.000550&type=&unitWidth=-6&ef=&formula=MACD&AT=1&imageType=KXL&timespan=1729046102
GET https://webquoteklinepic.eastmoney.com/GetPic.aspx?nid=1.600611&type=&unitWidth=-6&ef=&formula=MACD&AT=1&imageType=KXL&timespan=1729046050

nid: 600沪 -> 1.code
     000深 -> 0.code
"""


from util.my_utils import http_get_req_origin
import time
import os

all_codes = {
    0: ['000550'],
    1: ['600611']
}

data_url_base = 'https://webquotepic.eastmoney.com/GetPic.aspx'

img_path = r'E:\temp\4'

for tag, codes in all_codes.items():
    for code in codes:
        resp = http_get_req_origin('%s?imageType=rc&type=&token=44c9d251add88e27b65ed86506f6e5da&nid=%s.%s&timespan=%d' % (data_url_base,tag,code, time.time()))
        if resp.status_code != 200:
            print("%s get failed" % code)
        png_file = os.path.join(img_path, code + '.png')
        with open(png_file, 'wb') as f:
            f.write(resp.content)
        print("%s get success: %s" % (code, png_file))
