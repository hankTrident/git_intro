# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 18:42:41 2020

@author: hankwu
"""
import os
import glob
import shutil
import re

k1=os.listdir('D:/WinSCp/To_Do_List/Field_test_office_img/thumb_down/Annotations/')#file多#用歸檔要改
k2=os.listdir('D:/WinSCp/To_Do_List/Field_test_office_img/thumb_down/JPEGImages/')#fil3少
for i in range(len(k1)):
    k1[i]=k1[i].replace('xml','jpg')


tree,tree_less={},{}
#(number_tree,k,y)
t=tuple
lis,x=[],[]
for i in range(4):
    for j in range(4):
         if i>=j:
               t=(i,j)
               #print(t)
               lis.append(t)
lis[-1]=(4,0)
dx=lis
for i in range(len(k1)//10):
      x+=dx
lis2=x

for j in range(0,10*(len(k1)//10),10):  #n=10*(len(k1)//10),要改n=30 3個tree 存16000data 
         for i in range(j,j+10): #0~9
             tree['{}'.format(k1[i])]=(j//10,lis2[i][0],lis2[i][1])
for z in range(10*(len(k1)//10),len(k1)):
             tree['{}'.format(k1[z])]=((j+10)//10,dx[z%10][0],dx[z%10][1])

kEy=list(tree.keys())             
kval=list(tree.values())             
tree_lis=sorted(tree.items())# 變列表
#print(tree)
#for key, value in tree.items():  #找值   
#    if value==(1656, 3, 2):
#         print(key)
#for x in tree.values():
#    if x==1:
#        print(x in tree.keys())

for i in range(len(k2)):     #比對組
         tree_less[k2[i]]=1

tree.update(tree_less)


c,c1=0,0


dx=[]
for key, value in tree.items(): 
       
    if value==1: 
            #print(key) 
            c+=1
    
    else:
        pass
print('The overlapping : %d 數量\n'%c) #改
('\n')
for key, value in tree.items(): 
       
    if value==1: 
       pass

    else:
        dx.append(key)
        print(key) #改
        c1+=1
print('The lose files : %d 數量'%c1)  #改

with open('D:/WinSCp/To_Do_List/small_voc/lose-fils.txt','w') as f :
    for i in range(len(dx)):
        f.write(dx[i]+'\n')







