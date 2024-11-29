# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: getKdata.py
@time: 2024/10/16 10:41

依赖： pip install opencv-contrib-python

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

import os
import time
import json

from gp.gp_code import all_codes, husheng_zhuban
from util.my_utils import http_get_req_origin, write_str, remove_fd, http_get_req_origin_retry
from util.obs_client import upload_to_obs

k_url_base = 'https://webquoteklinepic.eastmoney.com/GetPic.aspx'

img_path = r'E:\1gp\png'

if not os.path.exists(img_path):
    os.makedirs(img_path, exist_ok=True)



def download_hangye(del_before=True, hangye_details=True):
    remove_fd(img_path, root_del=False)

    # 行业按照资金流排行
    resp = http_get_req_origin(r'https://push2.eastmoney.com/api/qt/clist/get?pn=1&pz=500&po=1&np=1&fields=f12%2Cf13%2Cf14%2Cf62&fid=f62&fs=m%3A90%2Bt%3A2')
    diffs = json.loads(resp.content)['data']['diff']
    write_str(os.path.join(img_path, 'paihang.txt'), '行业板块排行榜\n' + json.dumps(diffs))

    length = len(diffs)
    for i in range(length):
        diff = diffs[i]
        code = diff['f12']
        tag = diff['f13']
        png_file = os.path.join(img_path, code + '_%s.png' % i)
        resp = http_get_req_origin_retry(
            '%s?nid=%s.%s&type=&unitWidth=-6&ef=&formula=MACD&AT=1&imageType=KXL&timespan=%d' % (k_url_base, tag, code, time.time()))

        with open(png_file, 'wb') as f:
            f.write(resp.content)
        print("[%s %s/%s] %s get success: %s" % (tag, i + 1, length, code, png_file))
    print('All hangye download end.')
    all_count = 0
    if hangye_details:
        print('Start to get hangye details...')
        for i in range(length):
            diff = diffs[i]
            code = diff['f12']
            name = diff['f14']
            detail_file = os.path.join(img_path, code + "_details")
            os.makedirs(detail_file, exist_ok=True)
            # 获取前50个
            resp = http_get_req_origin(r'https://push2.eastmoney.com/api/qt/clist/get?fid=f62&po=1&pz=100&pn=1&np=1&fltt=2&invt=2&fs=b%3A' + code + '&fields=f12%2Cf14%2Cf62%2Cf66%2Cf72%2Cf13')
            diffs_detail = json.loads(resp.content)['data']['diff']
            # 过滤掉非沪深主板的数据
            new_diffs_detail = []
            for diff_ in diffs_detail:
                if diff_['f12'] in husheng_zhuban:
                    new_diffs_detail.append(diff_)

            write_str(os.path.join(detail_file, 'paihang.txt'), name + ' 行业排行榜\n' + json.dumps(new_diffs_detail))
            print('[%s] -> origin diff:%s, filter diff:%s' % (code, len(diffs_detail), len(new_diffs_detail)))

            length_detail = len(new_diffs_detail)
            all_count += length_detail
            for i_detail in range(length_detail):
                diff_detail = new_diffs_detail[i_detail]
                code_detail = diff_detail['f12']
                tag_detail = diff_detail['f13']
                png_file = os.path.join(detail_file, code_detail + '_%s.png' % i_detail)
                resp_detail = http_get_req_origin_retry(
                    '%s?nid=%s.%s&type=&unitWidth=-6&ef=&formula=MACD&AT=1&imageType=KXL&timespan=%d' % (
                    k_url_base, tag_detail, code_detail, time.time()))

                with open(png_file, 'wb') as f:
                    f.write(resp_detail.content)
                print("[%s] -> [%s %s/%s] %s get success: %s" % (code, tag_detail, i_detail + 1, length_detail, code_detail, png_file))
            print('[%s] -> All detail download end.' % code)

        print('hangye count:%s, details: %s' % (length, all_count))





def download_upload(upload=False):
    for f in os.listdir(img_path):
        if f.endswith('new.png'):
            new_f = f.replace('_new','')
            print('%s -> rename to: %s' % (f, new_f))
            os.rename(os.path.join(img_path,f),os.path.join(img_path,new_f))


    counts = {}
    for tag, codes in all_codes.items():
        length = len(codes)
        counts[tag] = length
        for i in range(length):
            code = codes[i]
            png_file = os.path.join(img_path, code + '_new.png')
            if os.path.exists(os.path.join(img_path, code + '.png')):
                os.remove(os.path.join(img_path, code + '.png'))
                # continue
            resp = http_get_req_origin(
                '%s?nid=%s.%s&type=&unitWidth=-6&ef=&formula=MACD&AT=1&imageType=KXL&timespan=%d' % (
                k_url_base, tag, code, time.time()))
            if resp.status_code != 200:
                print("[%s %s/%s] %s get failed" % (tag, i + 1, length, code))

            with open(png_file, 'wb') as f:
                f.write(resp.content)
            print("[%s %s/%s] %s get success: %s" % (tag, i + 1, length, code, png_file))

    if upload:
        print('All download success, start upload to obs.')
        for f in os.listdir(img_path):
            upload_to_obs(os.path.join(img_path, f), r'vpp/1batchSynth/test/k/' + f)
        print('Upload to obs success.')
    else:
        print('All png download success :%s.' % counts)


def clean():
    for f in os.listdir(img_path):
        os.remove(os.path.join(img_path, f))
    print("%s clean success" % img_path)


if __name__ == '__main__':
    download_hangye(False)