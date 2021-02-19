# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 10:32:19 2020

@author: hankwu
"""
import matplotlib.pyplot as plt
import cv2
import numpy as np
import math
import glob
from zero_one import zero_one
from xrange import xrange
 
def psnr1(img1, img2):
   #mse = np.mean((img1 - img2) ** 2 )
   mse=np.mean((img1/1.0 - img2/1.0) ** 2 )
   if mse < 1.0e-10:
      return 100
   return 10 * math.log10(255.0**2/mse)
 
def psnr2(img1, img2):
   mse = np.mean( (img1/255. - img2/255.) ** 2 )
   if mse < 1.0e-10:
      return 100
   PIXEL_MAX = 1
   return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))
name=['Lpalm_1','Lthumb-up','okay','Rthumb-up','stop','the one']#os.listdir(母資料)
img_x_list,gt_x=[],[]
for i in range(len(name)):
    dx=glob.glob('D:/HANK/raw/{}/jpg/*.jpg'.format(name[i]))
    dy=glob.glob('C:/Users/HankWu/Desktop/IRsubject2/{}(/JPEGImages/*.jpg'.format(name[i]))
    img_x_list+=dx
    gt_x+=dy

gt_t= cv2.imread(gt_x[13146])
img_t= cv2.imread(img_x_list[13146])
print(psnr1(img_t,gt_t))
print(psnr2(img_t,gt_t))
#
index=[x for x in range(len(img_x_list))]
op=zero_one(5) #要改大於len(list)
op=[x+40 for x in op]
index_40=[x for x in range(40-1,40+2)]
line_1=index_40+op[0:len(img_x_list)-len(index_40)]
index_50=[x for x in range(40-2,40+2)]
line_2=index_50+op[0:len(img_x_list)-len(index_50)]

yy_30=[30 for x in range(len(img_x_list))]
yy_20=[20 for x in range(len(img_x_list))]
yy_60=[60 for x in range(len(img_x_list))]
xx_100=[3170 for x in range(len(img_x_list))]
xx_200=[3170+1811 for x in range(len(img_x_list))]
xx_300=[3170+1811+976 for x in range(len(img_x_list))]
xx_400=[3170+1811+976+1572 for x in range(len(img_x_list))]
xx_500=[3170+1811+976+1572+732 for x in range(len(img_x_list))]
xx_600=[3170+1811+976+1572+732+4886 for x in range(len(img_x_list))]
y=[]
for i  in range(len(img_x_list)):
#gt = cv2.imread('C:/Users/HankWu/Downloads/800px-Taiwan_Taoyuan_International_Airport_hangar_5.jpg')
#img= cv2.imread('C:/Users/HankWu/Downloads/800px-Taiwan_Taoyuan_International_Airport_hangar_1.jpg')
      gt= cv2.imread(gt_x[i])
      img= cv2.imread(img_x_list[i])
      ps=psnr1(img,gt)
      y.append(ps)
mm=round(sum(y)/len(y))
plt.plot(index,y,label='PSNR Value/Avr={}dB'.format(mm))
plt.plot(index,yy_30)
#plt.plot(index,yy_60)
plt.plot(xx_100,line_1,label='{}'.format(name[0]))
plt.plot(xx_200,line_2,label='{}'.format(name[1]))
plt.plot(xx_300,line_1,label='{}'.format(name[2]))
plt.plot(xx_400,line_2,label='{}'.format(name[3]))
plt.plot(xx_500,line_1,label='{}'.format(name[4]))
plt.plot(xx_600,line_2,label='{}'.format(name[5]))
plt.legend()
plt.show