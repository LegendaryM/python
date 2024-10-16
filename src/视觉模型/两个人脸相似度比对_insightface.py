# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: 两个人脸相似度比对_dlib.py
@time: 2023/9/5 15:50
"""
import cv2
import numpy as np
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image
import os

app = FaceAnalysis(root='.', providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])  # 需要下载模型
app.prepare(ctx_id=0, det_size=(640, 640))

def get_image_features(image_np):
    if len(image_np.shape) != 3:
        app.logger.error(f"image shape: {image_np.shape} is not RGB!")
        return None

    list_of_features = app.get(image_np) # 获取图片人脸特征
    results_image = []
    for features in list_of_features:
        feature_dict = {'det_score': features.det_score,
                        'normed_embedding': features.normed_embedding
                        }
        results_image.append(feature_dict)

    return results_image

def cosine_similiarity(a, b):
    if a.shape != b.shape:
        app.logger.error(f"array {a.shape} shape not match {b.shape}")
    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)

    similiarity = np.dot(a, b.T)/(a_norm * b_norm)

    result = similiarity[0][0]
    return result

def compare(img1_path, img2_path):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    features_image1 = get_image_features(img1)
    features_image2 = get_image_features(img2)

    embedding1 = features_image1[0]['normed_embedding'].reshape(1, 512).astype(np.float32)
    embedding2 = features_image2[0]['normed_embedding'].reshape(1, 512).astype(np.float32)

    similiarity = float(cosine_similiarity(embedding1, embedding2))

    print(similiarity)

if __name__ == '__main__':
    compare('./data/face3.png', './data/face4.png')

