#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
# import torch
# import


x = np.array([-2,2])
w = np.array([1,2])
b = np.array([1,2])
z = w.T * x + b
print(np.where(z > 0, z, 0))











