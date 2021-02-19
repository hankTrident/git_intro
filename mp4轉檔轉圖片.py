# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 01:55:05 2020

@author: Wish
"""
from moviepy.editor import VideoFileClip as vclp
from moviepy.editor import concatenate_videoclips as concat
from moviepy.video import *
from moviepy.video.fx.all import crop
import os
import moviepy.editor as mpe
import re
import imageio
import glob
from natsort import natsorted
##先建子資料夾放入影片#
def mp4To():
    """convert to picutres from video by frame"""
    
    video=[]
    #dir_fr='C:/Users/HankWu/Videos/GINO/Gino1124/'  #母檔案料夾#要改
    dir_fr='D:/WinSCp/To_Do_List/Gino1126/'
    name = os.listdir(dir_fr)
    for i in range(len(name)):
           if name[i].endswith(('.exe','.rar','.zip','.txt','.jpg','.mp3','.csv')):
               pass

           else:
                dir1=dir_fr+name[i]+'/'   #子檔案料夾# #os.sep='/'
                #dir1='C:/Users/Wish/Documents/hand3_AME/'
                if os.path.exists(dir1):
                      dir=dir1+'JPEGImages'+os.sep #可改檔名
                for j in range(1,50):       
                     if os.path.exists(dir):
                        dir=dir1+'JPEGImages%d'%j+os.sep  ##輸出到每個子檔案料夾image 可改
                os.makedirs(dir)           
                name1 = os.listdir(dir1)
                for z in range(len(name1)):
                      if name1[z].endswith('.avi'):#改target resolution(720,720)
            #             clip1=vclp(dir1+'{}'.format(name1[i]),target_resolution=(720,720))
                         clip1=vclp(dir1+'{}'.format(name1[z]))
                         t=clip1.duration
                         FPS=clip1.fps
                         #clip1=clip1.subclip(0.5,t-0.5) #前後裁掉 減去30sec=0.5
                         clip1.write_images_sequence(dir+name[i]+'_{}'.format(z)+'_%04d.jpg')
                         video.append(clip1)          #jpg,png
                         #Write 可設fps 剪多減少 _%04d.jpg(04d位數)
                      else:
                            pass
    print('Time :',t,'fps :',FPS)                        
if __name__ =="__mp4To__":
    mp4To()

'''
.mp4 , 'libx264','mpeg4'(fast)
.avi , 'rawvideo','png'
.ogv , 'libvorbis'
.webm , 'libvpx' 
'''

#==========================================圖片合成影片                                          
dir='J:/gino/train/JPEGImages/m1_stop_1/'
file_list=glob.glob(dir+'*.jpg') #path
file_list_sorted = natsorted(file_list,reverse=False)                                                              
clips=[mpe.ImageClip(m).set_duration(1/10) for m in file_list_sorted]                                                              
video=concat(clips,method='compose')  #=925(資料夾張數)/30.85(目標時間) 轉多轉少
video.duration=round(1025/10,2)  
#os.mkdir('C:/Users/Wish/Videos/mp4/'+dir.split('JPEGImages/')[-1])
video.write_videofile('C:/Users/Wish/Videos/mp4/'+dir.split('JPEGImages/')[-1]+'output.mp4'
                      ,fps=10)#fps影響張數
    
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 