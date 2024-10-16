# -*- coding: utf-8 -*-

"""
pip install gradio -i https://pypi.tuna.tsinghua.edu.cn/simple

@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: gradio_web.py
@time: 2023/12/13 14:55
"""

import gradio as gr
import numpy as np


# demo1:
# def greet(name):
#     return "Hello, " + name + "!"

# iface = gr.Interface(fn=greet, inputs="text", outputs="text")
# demo = gr.Interface(
#     fn=greet,
#     # 自定义输入框
#     # 具体设置方法查看官方文档
#     inputs=gr.Textbox(lines=3, placeholder="Name Here...",label="my input"),
#     outputs="text",
# )

# demo2: 该函数有3个输入参数和2个输出参数
# def greet(name, is_morning, temperature):
#     salutation = "Good morning" if is_morning else "Good evening"
#     greeting = f"{salutation} {name}. It is {temperature} degrees today"
#     celsius = (temperature - 32) * 5 / 9
#     return greeting, round(celsius, 2)
#
# demo = gr.Interface(
#     fn=greet,
#     #按照处理程序设置输入组件
#     inputs=["text", "checkbox", gr.Slider(0, 100)],
#     #按照处理程序设置输出组件
#     outputs=["text", "number"],
# )

# demo3: 图像

# def sepia(input_img):
#     #处理图像
#     sepia_filter = np.array([
#         [0.393, 0.769, 0.189],
#         [0.349, 0.686, 0.168],
#         [0.272, 0.534, 0.131]
#     ])
#     sepia_img = input_img.dot(sepia_filter.T)
#     sepia_img /= sepia_img.max()
#     return sepia_img
# #shape设置输入图像大小
# demo = gr.Interface(sepia, gr.Image(width=200, height=200), "image")

# demo4: 多tab页
def flip_text(x):
    return x[::-1]
def flip_image(x):
    return np.fliplr(x)
def flip_image2(x):
    return x
with gr.Blocks() as demo:
    #用markdown语法编辑输出一段话
    gr.Markdown("Flip text or image files using this demo.")
    # 设置tab选项卡
    with gr.Tab("Flip Text"):
        #Blocks特有组件，设置所有子组件按垂直排列
        #垂直排列是默认情况，不加也没关系
        with gr.Column():
            text_input = gr.Textbox()
            text_output = gr.Textbox()
            text_button = gr.Button("Flip")
    with gr.Tab("Flip Image"):
        #Blocks特有组件，设置所有子组件按水平排列
        with gr.Row():
            image_input = gr.Image()
            image_output = gr.Image()
        image_button = gr.Button("Flip")
        login_button = gr.Button("login")
    #设置折叠内容
    with gr.Accordion("Open for More!"):
        gr.Markdown("Look at me...")
    text_button.click(flip_text, inputs=text_input, outputs=text_output)
    image_button.click(flip_image, inputs=image_input, outputs=image_output)
    login_button.click(flip_image2, inputs=text_input, outputs=text_output)


#账户和密码相同就可以通过
def same_auth(username, password):
    return username == '1' and password == '2'

demo.launch(server_name='0.0.0.0', server_port=8000, show_error=True,
            auth=same_auth,auth_message="username and password must be the same")
