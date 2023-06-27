# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: 知乎视频.py
@time: 2023/6/25 16:14
"""

from util.my_utils import http_get_req,get_current_time
from util.js_utils import get_js_context
import hashlib


def parse_data(datas):
    for data in datas:
        title, voteup_count, comment_count, link_url,playlist = data['title'], data['voteup_count'], data['comment_count'], data['link_url'], data['video']['playlist']
        if voteup_count < 200 and comment_count < 100:
            # print(title, 'voteup_count:', voteup_count, 'comment_count:', comment_count, 'vc小于200 and cc小于100, skip')
            continue

        if 'hd' in playlist:
            playlist_url = playlist['hd']['url']
        elif 'ld' in playlist:
            playlist_url = playlist['ld']['url']
        else:
            playlist_url = playlist['sd']['url']
        print('============', title, link_url, playlist_url)

js_context = get_js_context(r'../util/知乎加密算法.js')

# 只需要修改url中的请求关键字即可
url = r'https://www.zhihu.com/api/v4/members/13850678320/zvideos?offset=0&limit=20&similar_aggregation=true&include=similar_zvideo%2Ccreation_relationship%2Creaction_instruction'
while True:
    md5_value = hashlib.md5(('101_3_3.0+%s+ACATVeS44xaPTkoDMUvRj5-s_6Yn0ic2BA8=|1686019302' % (
        url.replace("https://www.zhihu.com", ''))).encode("utf-8")).hexdigest()
    params = {
                 'Cookie': r'_zap=3fb424c3-d1ab-4dee-8893-143be164b480; d_c0=ACATVeS44xaPTkoDMUvRj5-s_6Yn0ic2BA8=|1686019302; YD00517437729195%3AWM_TID=8IFyesdZnONAABEUEELUlcNQUj6qQg6y; YD00517437729195%3AWM_NI=v%2Boh4V3fBjesaWBuToFDBj3tZkYymjnJPRFm7K73ESUxOL3mGeXQpFP3aMy9SuyBegeqWjs%2FtRbdLnDFG3U8GRRsut1nNto7oy17YmGGMnOsvCV1vYvCEynLLovm0fvFWEs%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee8eef4da38c888db374ada88bb7d55a928e8aadc83c8f96a990e54297eeae96c92af0fea7c3b92ab6f5a189b75ef1ba8e8be879a3898e96d765869c8e8bb2809ab5979af062ae96a0b3c567f595f9d4c85997a881adb26785bb98b2f34e94edafaefc3391abb7a3e86da7af998bf225b88eae85cf66889a89d4d834858e9e94f880f3b28295ee3dada7ffd8dc678599838fce79b69d9ad2f553b69d8b9aed4890b1ba8eb36eb69a99a6f237e2a3; __snaker__id=uuXrLqMNcajUQVG0; gdxidpyhxdE=NpkE%5ClD6mqWwHqVux5%5C9NlLMmQQw8iyo%5CZ%2B5hWTtCQG%2FeT9qaaP2ZBAzuaxttXMotEnmhXyd6i%5CphTwGwlmiBbcd7YNe9PxIfaI17StW95wd5vIxZlXUWJd%2FZNSzk11Ty6TgD%2BTePoZys0xH02y9GQ5WaUTzJPeza0vTbMymRcdYZcw%5C%3A1686192600820; captcha_session_v2=2|1:0|10:1686191703|18:captcha_session_v2|88:cDlmaGRxUWpXMmN4TzBoQnB1SjNjNDlwQXo0M1pOVzQ5ZVl2NldBZ1VjSEM4RjFUK2Vvemg4d0RPbVA1STB5Ng==|d93354536b6157a254b3be8e8b33692e2f3864f8607c1f2e13cf79975b2f5b78; q_c1=5ae2e3a43d7f42e7a73fd0d7be4380fc|1686191881000|1686191881000; z_c0=2|1:0|10:1686194830|4:z_c0|92:Mi4xR1ZLTE5BQUFBQUFBSUJOVjVMampGaVlBQUFCZ0FsVk5DWTF1WlFBaFRoZGs4WkQ4RjM4SGU4c2s5V0t0WUlYM1ZR|77004677e6147921641a2bc08dbe43ccb34b31a054a182ea9d97a98b0a272990; tst=v; _xsrf=1126a663-f185-407b-b611-497e3cd85482; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1686019303,1686549969,1686721701; SESSIONID=aDKgkiov4O5ABXbQMLgqtckMwDUOrDl9j3Qr3Li3UNM; JOID=U1gcBkNzH68Eds53XncHcFmRcpxAE1LobhSmESROUZNJOZ8UBlwxPmR-xnJff_kzTKcucTn1Rwxah9bzPOrJTvc=; osd=UlgRCkhyH6IIfc93U3sMcVmcfpdBE1_kZRWmHChFUJNENZQVBlE9NWV-y35Ufvk-QKwvcTT5TA1aitr4PerEQvw=; KLBRSID=cdfcc1d45d024a211bb7144f66bda2cf|' + str(
                     get_current_time(show_type='s')) + '|1687671891',
             'Sec-Ch-Ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                         'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': "Windows",
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Ab-Param': '',
    'X-Ab-Pb': 'Cgo7ArcDiwUnB/gMEgUCAAAAAA==',
    'X-Requested-With': 'fetch',
    'X-Zse-93': '101_3_3.0',
    'X-Zse-96': '2.0_%s' % (js_context.call('D', md5_value)),

    }
    resp = http_get_req(url, headers=params)
    if 'error' in resp:
        print(resp, md5_value)
        print(params)
        break
    datas, next_url, totals, is_end = resp['data'], resp['paging']['next'], resp['paging']['totals'], resp['paging']['is_end']
    parse_data(datas)
    if is_end:
        break
    url = next_url


