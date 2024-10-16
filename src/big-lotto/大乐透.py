# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: 大乐透.py
@time: 2023/11/29 13:55
    游戏规则： （官网 https://www.lottery.gov.cn/dlt/index.html）
        前5 后2
        前区号码由01—35共三十五个号码组成，后区号码由01—12共十二个号码组成。
        每注基本投注金额人民币2元。
"""
from util.my_utils import http_get_req, sleep, write_list, read_list


def get_history_response():
    gameNo = 85
    url = r'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=%s&provinceId=0&pageSize=30&isVerify=1&pageNo=%s'
    historys = []
    for i in range(0, 85):
        response = http_get_req(url % (gameNo, i))
        for res in response['value']['list']:
            # print(res['lotteryDrawTime'], res['lotteryDrawNum'], res['lotteryDrawResult'])
            historys.append('%s<>%s<>%s' % (res['lotteryDrawTime'], res['lotteryDrawNum'], res['lotteryDrawResult']))

        sleep(2)
    return historys

# historys = get_history_response()
# historys = ['11','2']
# write_list(historys, './response.txt')

historys = read_list('./response.txt')
print(historys)