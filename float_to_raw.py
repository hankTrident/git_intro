# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 16:56:27 2020

@author: hankwu
"""

import os
import csv
from tqdm import tqdm
import numpy as np
import cv2
import matplotlib.pyplot as plt
'''
SSD  :  320*224
yolo v3 : 320*240
'''

def float_to_raw(float_image, w, h):
    byte_image = bytearray(np.zeros((h*w), dtype=bytes))
    temp_image = np.reshape(float_image, (h*w))
    i=0
    while i<len(temp_image):
        byte_image[i] = int(np.clip(round(temp_image[i]), 0, 255))
        i+=1
    byte_image = np.reshape(byte_image, (h,w))
    del(temp_image)
    return byte_image

floder_path = 'SUM/20/thumb_down/'
save_floder_path = 'thumbdown/'

img_floder = os.listdir(floder_path)
img_count = 0
for raw_img in img_floder:
    img_count += 1
    if img_count %3 ==0:  # %4 ,%3(FPS), %2 
        try:
            if raw_img.endswith('.raw'):
                print(raw_img)
                raw_path = floder_path +  raw_img
                ori_img = open(raw_path, 'rb')
                
                rows = 224
                cols = 320
                ori_img = np.fromfile(ori_img, dtype=np.uint8,count=rows*cols)
                ori_img = ori_img.reshape((rows,cols))

                cv2.imwrite(save_floder_path + raw_img.replace('raw','png') ,ori_img)
        except:
            continue
