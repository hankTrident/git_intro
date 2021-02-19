# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 21:37:40 2020

@author: Wish
"""

import xml.etree.ElementTree as ET
import pandas as pd
import os

###先準備一XML檔 CSV加入table image檔
dir_fr='D:/WinSCp/To_Do_List/Background_2/palm_left/'
df=pd.read_csv(dir_fr+'palm_left.csv')
k=df['table']
#
t={}
for i in range(len(k)):
       s=k[i].split(';')
       s.pop(-1)
       if len(s)//6==1:
           t[str(s[0])]=(s[1:5])
       elif len(s)//6==2:
           t[str(s[0])]=(s[1:5],s[7:11])
       elif len(s)//6==3:
           t[str(s[0])]=(s[1:5],s[7:11],s[13:17])


xml_1=ET.parse(dir_fr+'template.xml')  #one box

root_1=xml_1.getroot()
obj_1=root_1.findall('object')
box_1=obj_1[0].find('bndbox') 
file=xml_1.findall('filename')
file[0].text

p=xml_1.findall('path')
p[0].text
                                                 #要改
list_name=os.listdir(dir_fr)

for i in range(len(list_name)):              #檔案名
       list_name[i]=list_name[i].replace('.jpg','')
os.mkdir(dir_fr+'Annotations/')
for i in range(len(t)): #原本t
   #
          s=k[i].split(';')
          box_1[0].text=t[str(s[0])][0]  #str
          box_1[1].text=t[str(s[0])][1]
          box_1[2].text=t[str(s[0])][2]
          box_1[3].text=t[str(s[0])][3]
          file[0].text=s[0]                              #後面要改
          p[0].text='/home/user/Desktop/classification/Gesture_2stage/stop_far/JPEGImages/'+s[0]
          #xml_1.write('C:/Users/Wish/Desktop/stop_far/Annotations/'+s[0].replace('.jpg','.xml'), encoding='UTF-8')
          xml_1.write(dir_fr+'Annotations/'+s[0].replace('.jpg','.xml'), encoding='UTF-8')
#    elif type(t[i])==tuple:                                #要改
#          box[0].text=t[i][0][0]  #str
#          box[1].text=t[i][0][1]
#          box[2].text=t[i][0][2]
#          box[3].text=t[i][0][3]
#          box1[0].text=t[i][1][0]
#          box1[1].text=t[i][1][1]
#          box1[2].text=t[i][1][2]
#          box1[3].text=t[i][1][3]#(x,y)
#          file[0].text=list_name[i]+'.jpg'
#          p[0].text='J:/新增資料夾/JPEGImages/'+list_name[i]+'.jpg'
#          xml.write('J:/新增資料夾/Annotations/out/'+list_name[i]+'.xml', encoding='UTF-8')


