# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: main.py.py
@time: 2024/10/17 15:19
"""

from gp.getKdata import clean, download_upload
from gp.send_email import send


def main(cmd):
    if cmd == 'clean':
        clean()
    else:
        download_upload()
        send()