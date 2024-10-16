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

# 发件人和收件人的邮箱地址
sender = 'dhpt_excep@163.com'
receiver = '443955274@qq.com'
password = "IOFAXILBUAPAJAIK"

# 创建邮件
message = MIMEMultipart()
message["From"] = sender
message["To"] = receiver
message["Subject"] = "自动发送邮件示例"

# 添加邮件正文
# message.attach(MIMEText("这是一封自动发送的邮件。", "plain"))
# 添加HTML邮件内容
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>HTML邮件示例</title>
</head>
<body>
    <h1>这是一封HTML格式的邮件</h1>
    <p>你可以在邮件中使用HTML标记来格式化内容。</p>
</body>
</html>
"""

message.attach(MIMEText(html_content, "html"))

# 连接到SMTP服务器
with smtplib.SMTP("smtp.163.com", 25) as server:
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, message.as_string())

print("邮件已发送成功！")