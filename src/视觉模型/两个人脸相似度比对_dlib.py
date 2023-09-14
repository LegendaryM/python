# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: 两个人脸相似度比对_dlib.py
@time: 2023/9/5 15:50
"""
import cv2
import dlib
import numpy as np

# 加载dlib预训练模型
predictor_path = 'shape_predictor_68_face_landmarks.dat'  # 替换为你自己的模型路径
face_rec_model_path = 'dlib_face_recognition_resnet_model_v1.dat'  # 替换为你自己的模型路径
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(predictor_path)
facerec = dlib.face_recognition_model_v1(face_rec_model_path)


# 计算两个人脸的相似度
def calculate_similarity(image_file1, image_file2):
    # 加载图像
    img1 = cv2.imread(image_file1)
    img2 = cv2.imread(image_file2)

    # 转换为RGB格式
    img1_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

    # 检测人脸并提取特征向量
    faces1 = detector(img1_rgb)
    faces2 = detector(img2_rgb)

    if len(faces1) == 0 or len(faces2) == 0:
        return None

    # face_descs1 = [facerec.compute_face_descriptor(img1_rgb, shape) for shape in sp(img1_rgb, faces1[0]).parts()]
    # face_descs2 = [facerec.compute_face_descriptor(img2_rgb, shape) for shape in sp(img2_rgb, faces2[0]).parts()]
    face_descs1 = facerec.compute_face_descriptor(img1_rgb, sp(img1_rgb, faces1[0]))
    face_descs2 = facerec.compute_face_descriptor(img2_rgb, sp(img2_rgb, faces2[0]))

    # 两张人脸特征向量的欧氏距离越小，说明两个人越相似。当欧氏距离小于某一个值时，则可以认为他们是同一个人
    distance1 = np.linalg.norm(np.array(face_descs1) - np.array(face_descs2))
    print(distance1)
    # 计算相似度
    # distance = dlib.distance(face_descs1[0], face_descs2[0])
    # similarity = 1 / (1 + distance)

    return distance1


# 测试代码
image_file1 = './data/face3.png'  # 替换为第一个人脸的图像文件路径
image_file2 = './data/face4.png'  # 替换为第二个人脸的图像文件路径

similarity = calculate_similarity(image_file1, image_file2)
print(f"The similarity between the two faces is: {similarity}")
