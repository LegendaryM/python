# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: 获取token.py
@time: 2023/5/22 10:30
"""

import os
import time
import json
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from ai_ability.config import *

def get_token(client):
   # 创建request，并设置参数。
   request = CommonRequest()
   request.set_method('POST')
   request.set_domain('nls-meta.cn-shanghai.aliyuncs.com')
   request.set_version('2019-02-28')
   request.set_action_name('CreateToken')

   try:
      response = client.do_action_with_exception(request)
      print(response)

      jss = json.loads(response)
      if 'Token' in jss and 'Id' in jss['Token']:
         token = jss['Token']['Id']
         expireTime = jss['Token']['ExpireTime']
         print("token = " + token)
         print("expireTime = " + str(expireTime))
   except Exception as e:
      print(e)

# 创建AcsClient实例
client = AcsClient(
   ali_aki,
   ali_aks,
   "cn-shanghai"
)

get_token(client)

