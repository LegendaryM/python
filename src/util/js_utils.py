# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: js_utils.py
@time: 2023/6/25 18:27
"""
import execjs # pip3 install PyExecJS


def js_from_file(file_name):
    """
    读取js文件
    :return:
    """
    with open(file_name, 'r', encoding='UTF-8') as file:
        result = file.read()

    return result


def get_js_context(file_name):
    # 编译加载js字符串
    # context1 = execjs.compile(js_from_file('./norm.js'))
    # 调用js代码中的add()方法，参数为2和3
    # 方法名：add
    # 参数：2和3
    # result1 = context1.call("add", 2, 3)
    return execjs.compile(js_from_file(file_name))


if __name__ == '__main__':
    context = get_js_context(r'知乎加密算法.js')
    result = context.call('D', '763f8681182ae6c0230f3dd9720e6599')
    print(result)