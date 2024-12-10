# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: getKdata.py
@time: 2024/10/16 10:41

依赖： pip install opencv-contrib-python
     pip install pillow

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

k_url_base = 'https://webquoteklinepic.eastmoney.com/GetPic.aspx'

img_path = r'E:\1gp\png'

if not os.path.exists(img_path):
    os.makedirs(img_path, exist_ok=True)


def resize_png(img_path):
    import cv2
    from PIL import Image
    cv_image = cv2.imread(img_path)

    new_img = cv2.resize(cv_image, (round(cv_image.shape[1] * 1.1), round(cv_image.shape[0] * 1.1)))
    cv_image_rgb = cv2.cvtColor(new_img, cv2.COLOR_BGR2RGB)

    # 将 NumPy 数组转换为 PIL 图像
    pil_image = Image.fromarray(cv_image_rgb)

    # 应用颜色量化，限制颜色数为 256，并转换为 'P' 模式（即 palette 模式）
    quantized_image = pil_image.quantize(colors=256)

    new_img_path = img_path.replace('_origin','')
    # 保存图像为 PNG 文件，保持调色板模式
    quantized_image.save(new_img_path, format='PNG')
    return new_img_path


def download_hangye(hangye_gegu_count_max=30, price_min=3, price_max=30, day_zhangfu_min=0.5):
    """
    :param hangye_gegu_count_max: 行业个股的下载的最大图片数
    :param descend_count: 当天下跌的下跌数据
    """
    remove_fd(img_path, root_del=False)

    # 行业按照资金流排行
    resp = http_get_req_origin(r'https://push2.eastmoney.com/api/qt/clist/get?pn=1&pz=500&po=1&np=1&fields=f12%2Cf13%2Cf14%2Cf62&fid=f62&fs=m%3A90%2Bt%3A2')
    diffs = json.loads(resp.content)['data']['diff']
    write_str(os.path.join(img_path, 'paihang.txt'), json.dumps(diffs))

    length = len(diffs)
    for i in range(length):
        diff = diffs[i]
        code = diff['f12']
        tag = diff['f13']
        png_file = os.path.join(img_path, code + '.png')
        resp = http_get_req_origin_retry(
            '%s?nid=%s.%s&type=&unitWidth=-6&ef=&formula=MACD&AT=1&imageType=KXL&timespan=%d' % (k_url_base, tag, code, time.time()))

        with open(png_file, 'wb') as f:
            f.write(resp.content)
        print("[%s %s/%s] %s get success: %s" % (tag, i + 1, length, code, png_file))
        time.sleep(0.2)
    print('All hangye download end.')
    all_count = 0

    print('Start to get hangye details...')
    for i in range(length):
        diff = diffs[i]
        code = diff['f12']
        name = diff['f14']
        detail_file = os.path.join(img_path, code + "_details")
        os.makedirs(detail_file, exist_ok=True)
        # 获取前50个
        resp = http_get_req_origin(r'https://push2.eastmoney.com/api/qt/clist/get?fid=f3&po=1&pz=100&pn=1&np=1&fltt=2&invt=2&fs=b%3A' + code + '&fields=f12%2Cf14%2Cf62%2Cf66%2Cf72%2Cf13%2Cf3%2Cf2')
        diffs_detail = json.loads(resp.content)['data']['diff']
        # 过滤掉非沪深主板的数据
        new_diffs_detail = []
        for diff_ in diffs_detail:
            if diff_['f12'] in husheng_zhuban:  # 选择当日上涨、主力净流入大于0、价格在区间内的
                if isinstance(diff_['f3'], str):
                    continue
                if diff_['f3'] > day_zhangfu_min and diff_['f2'] >= price_min and diff_['f2'] <= price_max:
                    new_diffs_detail.append(diff_)
            if len(new_diffs_detail) >= hangye_gegu_count_max: # 超过个股选择数量时，跳过
                break

        write_str(os.path.join(detail_file, 'paihang.txt'), json.dumps(new_diffs_detail))
        print('[%s] -> origin diff:%s, filter diff:%s' % (code, len(diffs_detail), len(new_diffs_detail)))

        length_detail = len(new_diffs_detail)
        all_count += length_detail
        for i_detail in range(length_detail):
            diff_detail = new_diffs_detail[i_detail]
            code_detail = diff_detail['f12']
            tag_detail = diff_detail['f13']
            png_file = os.path.join(detail_file, code_detail + '.png_origin')
            resp_detail = http_get_req_origin_retry(
                '%s?nid=%s.%s&type=&unitWidth=-6&ef=&formula=MACD&AT=1&imageType=KXL&timespan=%d' % (
                k_url_base, tag_detail, code_detail, time.time()))

            with open(png_file, 'wb') as f:
                f.write(resp_detail.content)
            new_png_file = resize_png(png_file)
            os.remove(png_file)

            print("[%s %s/%s] -> [%s %s/%s] %s get success: %s" % (code, i,length, tag_detail, i_detail + 1, length_detail, code_detail, new_png_file))
            time.sleep(0.2)
        print('[%s] -> All detail download end.' % code)

        print('hangye count:%s, details: %s' % (length, all_count))


def clean():
    for f in os.listdir(img_path):
        os.remove(os.path.join(img_path, f))
    print("%s clean success" % img_path)


if __name__ == '__main__':
    download_hangye()