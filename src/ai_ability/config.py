# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: config.py
@time: 2023/3/14 12:46
"""

import os
from configparser import ConfigParser

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini")

cf = ConfigParser()
cf.read(file_path, encoding='utf-8')

# log_path = cf.get('path', 'log')
# task_path = cf.get('path', 'task')

ali_aki = cf.get('ali', 'access_key_id')
ali_aks = cf.get('ali', 'access_key_secret')
ali_ak = cf.get('ali', 'app_key')
