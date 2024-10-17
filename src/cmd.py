# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: cmd.py
@time: 2024/10/17 15:15
"""

from gp.main import main
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("param: clean/make")
    else:
        main(sys.argv[1])