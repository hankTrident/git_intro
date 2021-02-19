# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 00:14:21 2020

@author: Wish
"""

from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np
import glob
from statistics import mean

def red_collect(): 
    list_redr,list_redl=[],[]
    list_file=glob.glob('C:/Users/Wish/Videos/GINO/yh/image/*.jpg')
    for i in range(len(list_file)):
             dir=list_file[i]
             filename=dir.split('image\\')[-1] #對上面image
             img2 = cv2.imread(dir)
                
             hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
             lower_green = np.array([150, 200, 200])
             upper_green = np.array([255, 255, 255])
             mask = cv2.inRange(hsv, lower_green, upper_green) 
             res = cv2.bitwise_and(img2, img2, mask=mask)
             #cv2.imshow('Result', res)
             #cv2.imshow('Mask', mask)
             #cv2.waitKey(0)
             #cv2.destroyAllWindows()
                
                
             qq=np.where(mask>=255)#index
             np.sum(qq[0])#(x2,y2)   
             rangex=np.where(qq[0]>=((np.max(qq[0])+np.min(qq[0]))/2))   #0~585
             y2=np.sum(qq[0][rangex[0][0]:len(qq[0])])/(len(qq[0])-rangex[0][0])#y2 282~585=585-281
             y1=np.sum(qq[0][0:rangex[0][0]])/(rangex[0][0])#x2 0~281                 
                
             np.sum(qq[1])#(x1,y1)
             x1=np.sum(qq[1][rangex[0][0]:len(qq[0])])/(len(qq[0])-rangex[0][0])#x1
             x2=np.sum(qq[1][0:rangex[0][0]])/(rangex[0][0])#y1
             #print(filename+str(round(x1))+';'+str(round(y1))+';'+str(round(x2))+';'+str(round(y2))+';0;0;')
             red_r=(round(x2),round(y1)) #=>(x2,y1) csv.defind
             red_l=(round(x1),round(y2))#=>(x1.y2)
         
             list_redr.append(red_r)
             list_redl.append(red_l)                                  
    return list_redr,list_redl 
      
list_redr,list_redl=red_collect()
x1,y2,x2,y1=[],[],[],[]
normal_dx,normal_dy=[],[]
#normal_dx=394-344
#normal_dy=547-331
for i in range(100): #len(list_redl)
    x1.append(list_redl[i][0])
    y2.append(-list_redl[i][1])
    x2.append(list_redr[i][0])
    y1.append(-list_redr[i][1])    
    normal_dx.append(list_redr[i][0]-list_redl[i][0])
    normal_dy.append(list_redl[i][1]-list_redr[i][1])
normal_dx_av=mean(normal_dx)

normal_dy_av=mean(normal_dy)

    
#x1_normal=[x1[x]+normal_dx[x] for x in range(len(x1))]     
#y2_normal=[y2[x]+normal_dy[x] for x in range(len(y2))]  
y2_normal=[x+normal_dy_av for x in y2]   
x1_normal=[x+normal_dx_av for x in x1]   
plt.plot(x1_normal,y2_normal,label='track3_1')#
plt.plot(x2,y1,label='track2')#
#plt.plot(x1,y2,label='track3')     
plt.legend()
plt.show()

dir='C:/Users/Wish/Videos/GINO/yh/image/frame0_0006.jpg'
img=Image.open(dir)
img=img.convert('RGB')
#img.show()
nimg=Image.new('RGB',img.size,(255,255,255))
w,h=img.size
a,dic={},{}
for i in range(w):
    for j in range(h):
        r,g,b=img.getpixel((i,j))
        t=r*255*255+g*255+b
        
        if t in a.keys():
            a[t]=a[t]+1
        else:
            a[t]=1
        
l=sorted(a.items())
for i in l:
    if(i[1]<500):
        dic[i[0]]=i[1]
        
plt.figure(1,figsize=(19,5))
plt.scatter(dic.keys(),dic.values(),linewidth=1)        
plt.legend()
plt.show()

for i in range(w):
    for j in range(h):
        r,g,b=img.getpixel((i,j))
        t=r*255*255+g*255+b
        if t< 7000000:
            nimg.putpixel((i,j),(r,g,b))
#        
nimg.show()        
        

filename=dir.split('/')[-1].replace('.jpg','.jpg;')
img2 = cv2.imread(dir)

# 畫出 RGB 三種顏色的分佈圖
color = ('b','g','r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img2],[i],None,[256],[0, 256])
    plt.figure(2,figsize=(19,5))
    plt.plot(histr, color = col)
    plt.xlim([0, 256])
    plt.show()        



hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
lower_green = np.array([150, 200, 200])
upper_green = np.array([255, 255, 255])
mask = cv2.inRange(hsv, lower_green, upper_green) 
res = cv2.bitwise_and(img2, img2, mask=mask)
#cv2.imshow('Result', res)
#cv2.imshow('Mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()


qq=np.where(mask>=255)#index
np.sum(qq[0])#(x2,y2)   
range=np.where(qq[0]>=((np.max(qq[0])+np.min(qq[0]))/2))   #0~585
y2=np.sum(qq[0][range[0][0]:len(qq[0])])/(len(qq[0])-range[0][0])#y2 282~585=585-281
y1=np.sum(qq[0][0:range[0][0]])/(range[0][0])#x2 0~281                 

np.sum(qq[1])#(x1,y1)
x1=np.sum(qq[1][range[0][0]:len(qq[0])])/(len(qq[0])-range[0][0])#x1
x2=np.sum(qq[1][0:range[0][0]])/(range[0][0])#y1
#print(filename+str(round(x1))+';'+str(round(y1))+';'+str(round(x2))+';'+str(round(y2))+';0;0;')
red_r=(round(x2),round(y1)) #=>(x2,y1) csv.defind
red_l=(round(x1),round(y2))#=>(x1.y2)
list_redr,list_redl=[],[]
list_redr.append(red_r)
list_redl.append(red_l)
#list_redr[1]-list_redr[0]

