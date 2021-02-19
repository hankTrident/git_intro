# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:39:38 2020

@author: hankwu
"""
from Foldercount_json import *



str1=['n_1',  'n_2',  'n_3'  ,'n_4'  
      ,'n_6'  ,'n_7' , 'n_8'  ,'n_9' , 'ok',
      'r_palm_down','r_palm_left','r_palm_right','r_palm_up',
      'r_thumb_left','r_thumb_right','stone','stop','thumb_down',
      'thumb_up']

str2=['n_2',  'n_3'  ,'n_4'  
      ,'n_6'  ,'n_7' , 'n_8'  ,'n_9' , 'ok',
      'r_palm_up','r_thumb_right','stone','stop','thumb_down',
      'thumb_up']
#folder=[]
#for i in range(len(str1)):  #generte folder依據
#    
#    try:
#       yt=llist(str1[i])
#       folder.append(yt)
#    except:
#        pass
    
#folder 無法定義
'155 cut, 14 fold, 6 sub-folder >取155*14*6'  
#a=0~13
for i in range(14):
    
    count=folder_move(i) #one folder 張數
    move_select_files(i,count,str2[i])
    
    
















