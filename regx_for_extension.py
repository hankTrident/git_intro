# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 18:45:10 2020

@author: hankwu
"""
import os
import re

'''
folder 不能有. error
先import moduale "from regxxxxx import * "
multi_regx(s[2]) > 找特定後綴 2>.xx 3>.xxx (常用)
multi_regx_ch(*s) |multi_regx_ch('.png',*s) >改後綴
ex:
    print(multi_regx_ch(*s))
    print(multi_regx_ch('.png',*s))
    print(multi_regx(s[3]))
    
    multi_regx_ch(*s)[0]==<file name>~~ but suffix different~
    multi_regx_ch(*s)==os.listdir
'''

#s=['blank','blank',r'.\w\w$',r'\D\w\w\w$',r'\D\w\w\w\w$','...$'] #the same
s=('.jpg','blank',r'.\w\w$',r'\D\w\w\w$',r'\D\w\w\w\w$','...$')#**'.jpg' 重要預設 
dir1='C:/Users/HankWu/Downloads/todo/1440/新增資料夾/'# 要改
final_name=os.listdir(dir1)

def multi_regx(a): # 
    alsufx=[]
    
    for i in range(len(final_name)):
        try:
            #regex=re.compile(r'\D\w\w\w$')
            regex=re.compile(a)
    #        regex_2=re.compile(r'\D\w\w$')
    #        regex_4=re.compile(r'\D\w\w\w$')
            match=regex.search(final_name[i])
            sufx=match.group(0)
            if sufx.find('.')!=-1: #代表存在
                prefix=final_name[i].split(sufx)[0]
                
                
                alsufx.append((prefix,sufx))
            print(sufx)
        except:
            pass
        
    return alsufx

def multi_regx_ch(a='.jpg',*args):  #input tuple形式> out list
    alsufx=[]
    suffix=[]
    for i in range(len(final_name)):
        try:
            #regex=re.compile(r'\D\w\w\w$')
            regex=re.compile(args[2])
    #        regex_2=re.compile(r'\D\w\w$')
    #        regex_4=re.compile(r'\D\w\w\w$')
            match=regex.search(final_name[i])
            sufx=match.group(0)
            if sufx.find('.')!=-1: #代表存在
                prefix=final_name[i].split(sufx)[0]
                
                suffix.append(prefix+a)
                alsufx.append((prefix,sufx))
            #print(sufx)
        except:
            pass
        
        try:
            #regex=re.compile(r'\D\w\w\w$')
            regex=re.compile(args[3])
    #        regex_2=re.compile(r'\D\w\w$')
    #        regex_4=re.compile(r'\D\w\w\w$')
            match=regex.search(final_name[i])
            sufx=match.group(0)
            if sufx.find('.')!=-1: #代表存在
                prefix=final_name[i].split(sufx)[0]
                
                suffix.append(prefix+a)
                alsufx.append((prefix,sufx))
            #print(sufx)
        except:
            pass
        
        try:
            #regex=re.compile(r'\D\w\w\w$')
            regex=re.compile(args[4])
    #        regex_2=re.compile(r'\D\w\w$')
    #        regex_4=re.compile(r'\D\w\w\w$')
            match=regex.search(final_name[i])
            sufx=match.group(0)
            if sufx.find('.')!=-1: #代表存在
                prefix=final_name[i].split(sufx)[0]
                
                suffix.append(prefix+a)
                alsufx.append((prefix,sufx))
            #print(sufx)
        except:
            pass
        
        
    #return alsufx #分離
    return suffix #合併

#同上
#alsufx=[]
#alsufx=alsufx+multi_regx(s[2])+multi_regx(s[3])+multi_regx(s[4])   
    
    
    
    
    
    
    
    
    
    
    
    
    
    