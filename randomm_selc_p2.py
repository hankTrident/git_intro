# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 20:08:54 2021

@author: Wish
"""

import numpy as np
import os
import shutil

def xx(a=10):
    t=np.random.randint(a,size=(2))[0]
    t1=np.random.randint(a,size=(2))[1]
    if t==t1:
            n_t=np.random.randint(a,size=(2))[0]
            n_t1=np.random.randint(a,size=(2))[1]
            t=n_t
            t1=n_t1
            #print(t,t1)
            return (t,t1)
            
            
    else:  #不相等
            #print('from xx() is {},{}'.format(t,t1))
            return (t,t1)
            
def xxx(a=10):
    y=xx(a)
    
    t=y[0]
    t1=y[1]
        
    if t==t1:
                
                n_t=np.random.randint(a,size=(2))[0]
                n_t1=np.random.randint(a,size=(2))[1]
                t=n_t
                t1=n_t1
                #print(t,t1)
                return (t,t1)
                
                
    else:
                #print('from xxx() is {},{}'.format(t,t1))
                return (t,t1)
            
def x_4(a=10):
    y=xxx(a)
    
    t=y[0]
    t1=y[1]
        
    if t==t1:
                
                n_t=np.random.randint(a,size=(2))[0]
                n_t1=np.random.randint(a,size=(2))[1]
                t=n_t
                t1=n_t1
                #print(t,t1)
                return (t,t1)
                
                
    else:
                #print('from xxxx() is {},{}'.format(t,t1))
                return (t,t1)

def random_final_o(a=10):  
    """generate random index of fix range 
       a=10  >>  0~9
       a=7  >>  0~6
       a=4  >>  0~3
    """
    
    indice=np.random.randint(a,size=(5))
    o={}
    
    inpu=(indice[0],indice[1],indice[2])
    
    #inpu=(indice[0],indice[1],indice[2],indice[3],indice[4])
    
    for i in range(len(inpu)):
       o[inpu[i]]='index_%d'%i
    
    #print('input')
    #print(o)
    if len(o)==3:
        pass
    elif len(o)==2:
        t=0
        o[t]='index_2'
        if len(o)==2:
           t=1
           o[t]='index_2'  
           if len(o)==2:
               t=2
               o[t]='index_2' 
               if len(o)==2:
                  t=3
                  o[t]='index_2' 
                  if len(o)==2:
                     t=4
                     o[t]='index_2' 
                     if len(o)==2:
                         t=5
                         o[t]='index_2' 
                         if len(o)==2:
                             t=6
                             o[t]='index_2' 
                             if len(o)==2:
                                 t=7
                                 o[t]='index_2' 
                                 if len(o)==2:
                                     t=8
                                     o[t]='index_2' 
                                     if len(o)==2:
                                         t=9
                                         o[t]='index_2' 
                                     else:
                                         pass
                                 else:
                                      pass
                                  
                             else:
                                  pass
                         else:
                              pass
                     else:
                          pass
                  else:
                      pass
               else:
                   pass
           else:
               pass
        else:
            pass
    elif len(o)==1:
         y=x_4(a)
         t=y[0]
         t1=y[1]
         #print(t)
         #print(t1)
        
         o[t]='index_1'
         o[t1]='index_2'
         
         if len(o)==2:
            t=0
            o[t]='index_2'
            if len(o)==2:
               t=1
               o[t]='index_2'  
               if len(o)==2:
                   t=2
                   o[t]='index_2' 
                   if len(o)==2:
                      t=3
                      o[t]='index_2' 
                      if len(o)==2:
                         t=4
                         o[t]='index_2' 
                         if len(o)==2:
                             t=5
                             o[t]='index_2' 
                             if len(o)==2:
                                 t=6
                                 o[t]='index_2' 
                                 if len(o)==2:
                                     t=7
                                     o[t]='index_2' 
                                     if len(o)==2:
                                         t=8
                                         o[t]='index_2' 
                                         if len(o)==2:
                                             t=9
                                             o[t]='index_2' 
                                         else:
                                             pass
                                     else:
                                          pass
                                      
                                 else:
                                      pass
                             else:
                                  pass
                         else:
                              pass
                      else:
                          pass
                   else:
                       pass
               else:
                   pass
         else:
            pass
    else:
        pass
         #print(len(o))
         #print(o)
    #new_dict = {v:k for k,v in dict.items()}   
    #print('out')
    #print(o)
    #list(o.keys())
    return tuple(o.keys())

def file_name(b=1): #one folder
    """a=數量"""
    
    dir='E:/Downloads1/10_3/'
    y=os.listdir(dir)
    for i in range(b):
        lis=(os.listdir(dir+'{}/'.format(y[i])))
        
        #print(y[i])
        #print(lis)
    return (y[i],lis)

# =check============================================================================
    
#with open('E:/Downloads1/out.txt','w')as f:
#     for i in range(100000):
#         g=random_final_o(5)
#         
#         f.write(str(list(g))+'\n')
#     
#with open('E:/Downloads1/out.txt','r')as f:
#     rr=f.readlines()
#     c=0
#     for i in range(len(rr)):
#     #len('[7, 4, 0]\n')==10
#         if len(rr[i])<10:
#             print(i,rr[i])
#             c+=1
#         else: 
#             
#             pass
#            # print("==================")
#            # print("It's ok!!")
#if c==0:
#          print("==================")
#          print("It's ok!!")
# =============================================================================
def random_pic_selc(a,b=1):
    """generate randoen pics to move
       a: index of bin 
       ex:10取3 >> 7取3 >> 4取3
       a:10 >> b:7 >>b:4
       b: folder cout
    """
    dir='E:/Downloads1/10_3/'
    dir_to='E:/Downloads1/selected_6/'
    
    go=file_name(b)
    folder=go[0]
    pics=go[1]
    
    rand=random_final_o(a)
    #(1,2,3)
    for i in range(len(rand)):
        #print(rand)
        if os.path.exists(dir_to):
                   pass
        else:
            os.makedirs(dir_to) 
            
        shutil.move(dir+folder+os.sep+pics[rand[i]],dir_to)
    
    print(dir+folder+os.sep)


#print('Already move!!')        
#for i in range(1,80): #移動(1038-1)個folder  target=2 >> 2+1 
##    try:
##        random_pic_selc(4,i)
##    except:
##        pass
#    #random_pic_selc(10,i) 
#    #random_pic_selc(7,i)
#    #random_pic_selc(4,i)
#
#    #========
#    random_pic_selc(1,i)  #10取一
    #=======


















