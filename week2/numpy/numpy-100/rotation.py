#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 12:31:33 2023

@author: nouman
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


im_path = "baboon.png"
im_array = cv2.imread(im_path)
print("original")
plt.imshow(cv2.cvtColor(im_array, cv2.COLOR_BGR2RGB))
plt.show()


# this image has 512 pixels width and 512 pixels height
# print(im_array.shape)

degrees = 135
rotated_im_array = im_array.copy()
for _ in range(degrees // 90):
    rotated_im_array = rotated_im_array.transpose(1, 0, 2)
    for j in range(0, rotated_im_array.shape[1] // 2):
        c = rotated_im_array[:, j, :].copy()
        rotated_im_array[:, j, :] = rotated_im_array[: , rotated_im_array.shape[1]-j-1, :]
        rotated_im_array[: , rotated_im_array.shape[1]-j-1, :] = c
print("rotated")
plt.imshow(cv2.cvtColor(rotated_im_array, cv2.COLOR_BGR2RGB))
plt.show()
