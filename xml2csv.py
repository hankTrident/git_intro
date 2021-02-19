# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:43:19 2020

@author: hankwu
"""
import cv2
import glob
import os
import xml.etree.ElementTree as ET
from moviepy.editor import VideoFileClip as vclp
from moviepy.editor import concatenate_videoclips as concat
import moviepy.editor as mpe
import re
import imageio
from natsort import natsorted
'''
xml cv2 看圖 改xml(正確)輸出csv paint "box"
'''
dir='D:/WinSCp/To_Do_List/12-30/palm_right/'
#dir1='C:/Users/HankWu/Desktop/IRsubject3/read/'
#os.makedirs(dir1+'vid/')
y=glob.glob(dir+'JPEGImages/*.png')
#os.makedirs(dir+'vid/')
x2=[]
file=open(dir+'palm_right.csv','w')#寫
w=glob.glob(dir+'Annotations/*.xml')
for i in range(len(w)):
             try:
                  xml=ET.parse(w[i])  #one box
                  root=xml.getroot()                                  #要改
                  obj=root.findall('object')           
                  box=obj[0].find('bndbox') #box1
                  dx1=int(box[0].text)  #(x,y)
                  dy1=int(box[1].text)  
                  dx2=int(box[2].text)      #(x1,y1))
                  dy2=int(box[3].text)
                  
                  file_name=xml.findall('filename')
                  file_name[0].text
                  p=xml.findall('path')
                  p[0].text
    #              img = cv2.imread(y[i])    
     #             cv2.rectangle(img, (dx1,dy1), (dx2,dy2), (0,0,255), 1)#BGR
      #            cv2.imwrite(dir1+'vid/'+y[i].split('\\')[-1], img)
                  file.write(file_name[0].text+';{};{};{};{};0;0;\n'.format(dx1,dy1,dx2,dy2))
             except:
                 pass
file.close()
              
