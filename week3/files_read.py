#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 17:19:13 2023

@author: nouman
"""
import cv2
import glob
import os
from numpy import random
path="/home/nouman/Downloads/training_batch/week 3"

files=os.path.join(path,"client_data")
for file in os.listdir(files):
        im = cv2.imread(os.path.join(files,file))
        width = im.shape[1]
        height = im.shape[0]
        new_width = int(width*0.5)
        new_height = int(height*0.5)
        x = random.randint(0,new_width)
        y = random.randint(0,new_height)