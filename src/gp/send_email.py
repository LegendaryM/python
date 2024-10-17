# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: send_email.py
@time: 2024/10/16 14:41

pip install secure-smtplib -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install PyEmail


"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from gp.gp_code import all_codes
import time

obs_base_url = r'https://digital-public.obs.cn-east-3.myhuaweicloud.com/vpp/1batchSynth/test/k'

def send():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>HTML邮件示例</title>
    </head>
    <body>
        <h1>这是一封HTML格式的邮件</h1>
        %s
    </body>
    </html>
    """

    img_content = ''
    for tag, codes in all_codes.items():
        for code in codes:
            img_content += '<img src="%s/%s.png" alt="%s" style="border:1px solid red"/><br /><br />' % (
            obs_base_url, code, code)
    html_content = html_content % img_content

    # 发件人和收件人的邮箱地址
    sender = 'dhpt_excep@163.com'
    receiver = '443955274@qq.com'
    password = "IOFAXILBUAPAJAIK"

    # 创建邮件
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = "%s" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    # 添加邮件正文
    # message.attach(MIMEText("这是一封自动发送的邮件。", "plain"))
    # 添加HTML邮件内容
    message.attach(MIMEText(html_content, "html"))

    # 连接到SMTP服务器
    with smtplib.SMTP("smtp.163.com", 25) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message.as_string())

    print("邮件已发送成功！")
