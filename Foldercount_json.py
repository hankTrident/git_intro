# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:03:05 2020

@author: hunk.wu
"""
import glob
import os
import shutil
import json
import pandas as pd


dir='D:/WinSCp/To_Do_List/'

'''
3層才可用
white_R/  
   'r_palm_right/
        hank_r_palm_right_30~80/
            20201006154555642~.png
            
folder 之間不能有檔案 bug
dict.pop('key') return value
'''
def llist(a):#找dir以下folder dir/a 
    
    
    uu=[]
    folder={}
#    str1=['hank_one_30','hank_one_80','Huck_one_30','Huck_one_80','masalu_one_30',
#          'masalu_one_80']
    
    #dir='D:/WinSCp/To_Do_List/white_R/'  #要改 shell層
    dir='D:/WinSCp/To_Do_List/S2_Mi_quick_test_new/' 
    dir2=dir+'%s/'%a
    str2=os.listdir(dir2)
    for i in range(len(str2)):
        
        dir3=dir2+'{}/'.format(str2[i])# 資料夾
        print(dir3)
        y=os.listdir(dir3)
        uu.append(len(y))
        for j in range((uu[i])):
            folder[y[j]]=str2[i]
#    for x,y in folder.items():
#            print(x,y)
        
        
        
    return 'total: %s'%sum(uu),uu,folder        

str1=['n_1',  'n_2',  'n_3'  ,'n_4'  
      ,'n_6'  ,'n_7' , 'n_8'  ,'n_9' , 'ok',
      'r_palm_down','r_palm_left','r_palm_right','r_palm_up',
      'r_thumb_left','r_thumb_right','stone','stop','thumb_down',
      'thumb_up']
str1=['Orientation_pitch','Orientation_roll','Orientation_yaw','Sidelight_2']
str3=['2020-12-25-Hank'] #第2層

#==============
#folder=[]
#for i in range(len(str1)):  #generte folder依據
#    
#    try:
#       yt=llist(str1[i])
#       folder.append(yt)
#    except:
#        pass
#=========================    


def IsRepeat(a):
    
    
    """ return the following dict is repeat or not (need 1 map(v.s)1 ) 
        a:selected folder    
    """
    
    dict=folder[a][2]
    f_name=list(dict.keys())
    ff=list(dict.values())
    for i in range(len(f_name)-1):
        f_name=sorted(f_name)
        if f_name[i]==f_name[i+1]:
            print(f_name[i],ff[i])
            return 1
        else: 
            return -1
        
#for i in range(len(folder)):
#    print(IsRepeat(i))    
    
#====================    
    
    
def gobak_folder():
    """ return ex-directory """
    
    dir='D:/WinSCp/To_Do_List/S2_Mi_quick_test_new - 複製/Orientation_yaw/' #要改
    y=glob.glob(dir+'**/*')
    for i in range(len(y)):
        shutil.move(y[i],dir)

def move_select_files(a,b,c):
    """ return ex-directory """
    
    
    dir='D:/WinSCp/To_Do_List/新增資料夾/Video/{}/'.format(c) #要改
    #dir_to='D:/WinSCp/To_Do_List/white_R(new)/r_palm_up/'
    dir_to='D:/WinSCp/To_Do_List/新增資料夾/Video(new2)/{}/'.format(c)
    
    if os.path.exists(dir_to):
           pass
    else:
            os.makedirs(dir_to) 
    
    y=glob.glob(dir+'**/*')#bigger
    
    dict=folder[a][2]
    dict2={}
    ff=list(dict.values())
    f_name=list(dict.keys())
    
    for i in range(len(ff)): 
        dict2[f_name[i]]=dir+ff[i]+'/'

              
    for i in range(len(b)):
            
            try:
                #shutil.move(dict2[b[i]]+b[i],dir) #取出來
                #shutil.move(dict2[b[i]]+b[i],dir_to) #取出來
                shutil.copy(dict2[b[i]]+b[i],dir_to)
            except:
                pass
                
              #return(dict2[b[i]])
        

    
def verse_gobak(a,c): #對應dict 找 folder[i][2] 改i 
    """ extract to direrent folders by <def_llist()> 
        a:selected folder    
    """
    
    
    #dir='D:/WinSCp/To_Do_List/white_R/r_palm_up/'
    dir='D:/WinSCp/To_Do_List/新增資料夾/Video/{}/'.format(c) #要改
    dict=folder[a][2]   #對應dict folder[i][2] 改i 
    dict2={}
    ff=list(dict.values())
    f_name=list(dict.keys())
    
    for i in range(len(ff)): 
        dict2[f_name[i]]=dir+ff[i]+'/'
    
   
    for key, value in dict2.items(): 
        
        if os.path.exists(value):
           pass
        else:
            os.makedirs(value) 
        try:
            shutil.move(dir+key,value)
        except:
            pass


def index_shift(a,b): 
    """ return certain index shift for range(x) in sub-folder
        a:selected folder
        b:shift derivation
    """
    
    
    c=0
    f1=[0]
    f2=[0+b] #要幾張從頭
    for i in range(12): #6 fold 一個循環##要改
        #p=(c,c+59*(i+1))
        k=folder[a][1]  #要改
        c+=k[i]
        f1.append(c)
        f2.append(c+b)   #要幾張
    for x,y in zip(f1,f2):
        print(x,y)
    return list(zip(f1,f2))
        


def folder_move(a):
    """move selected number pictures folder by <def index_shift>
       a:selected folder   
    """
    
    
    dict=folder[a][2]
    ff=list(dict.values())
    f_name=list(dict.keys())
    
    index_list=index_shift(a,320) #要改a 樟樹
    
    all=[]
    
    for i in range(len(index_list)):
        
        all+=(f_name[index_list[i][0]:index_list[i][1]])
    #return(f_name[index_list[0][0]:index_list[0][1]])
    return all
    
    
str2=['n_2',  'n_3'  ,'n_4'  
      ,'n_6'  ,'n_7' , 'n_8'  ,'n_9' , 'ok',
      'r_palm_up','r_thumb_right','stone','stop','thumb_down',
      'thumb_up']


#=======================要季的關掉
'155 cut, 14 fold, 6 sub-folder >取155*14*6' 
#a=0~13
#for i in range(1): #multi-folder
#    
#    count=folder_move(i) #one folder 張數
#    move_select_files(i,count,str3[i]) #改str1
#    #verse_gobak(i,str2[i])

#============================


def csvMap():
    """return csv map"""
    
    dir_fr='D:/WinSCp/To_Do_List/white_R/n_1(/'
    df=pd.read_csv(dir_fr+'n_1.csv')
    col=list(df.columns.values)
    df=df.rename(columns={col[0]:'table'})
    df1=pd.DataFrame(col,columns=['table'])
    df=df1.append(df,ignore_index=True)
    k=df['table']
    csv_map={}
    csv_map_tric=lambda x,y,index:[x,y,index]
    ext=col[0].split(';')[0]# 有繼承
    
    def jpg():
        
        for i in range(len(k)):
       
            name=k[i].split(';')[0] #name
            x1=k[i].split('.jpg;')[-1].split(';')[0]  #x1
            y1=k[i].split('.jpg;')[-1].split(';')[1]  #y1
            x2=k[i].split('.jpg;')[-1].split(';')[2]  #x2
            y2=k[i].split('.jpg;')[-1].split(';')[3]  #y2
            x1=int(x1)
            x2=int(x2)
            y1=int(y1)
            y2=int(y2)
            key = csv_map_tric(name,(x1,y1,x2,y2),i)[0]
            value = csv_map_tric(name,(x1,y1,x2,y2),i)[1]
            index = csv_map_tric(name,(x1,y1,x2,y2),i)[2]
            csv_map[key] = value
         
        return csv_map
    
    def png():
    
        for i in range(len(k)):
            name=k[i].split(';')[0] #name
            x1=k[i].split('.png;')[-1].split(';')[0]  #x1
            y1=k[i].split('.png;')[-1].split(';')[1]  #y1
            x2=k[i].split('.png;')[-1].split(';')[2]  #x2
            y2=k[i].split('.png;')[-1].split(';')[3]  #y2
            x1=int(x1)
            x2=int(x2)
            y1=int(y1)
            y2=int(y2)
            key = csv_map_tric(name,(x1,y1,x2,y2),i)[0]
            value = csv_map_tric(name,(x1,y1,x2,y2),i)[1]
            index = csv_map_tric(name,(x1,y1,x2,y2),i)[2]
            csv_map[key] = value
    
        return csv_map 
    
    if ext.endswith('.png'):
        return png()
    
    elif ext.endswith('.jpg'):
          return jpg()
    else:
        pass
    



     
def ex_json(a=0):
    """ export json file coontain label img /Date etc.."""
    'csv .py 吐出來 combiniation'
    core_dict={}
    shell_dict={}
    
    
        
    core,temp_2,temp_3,shell={},{},{},{}
   # '1th, 2nd ,  3rd,  4th'
    temp_2_1={}
    
    folder_value=list(folder[a][2].values())
    folder_key=list(folder[a][2].keys())
    
    
    a_dict={y:x for x,y in folder[a][2].items()}
    aa=list(a_dict.keys())
    aa=sorted(aa)
    
    H=csvMap()#****上面
    csv_value=list(H.values())
    csv_key=list(H.keys())
    
    for i in range(len(H)):
        y=lambda x,y,z,w:{x:y,z:w}
        #core['bounding box']=csv_value#from csv  box  
        #core['folder']=folder_value    #from folder[i][2]
        core=y('bounding box',csv_value[i],'folder',folder_value[i])
        
        temp_2[folder_key[i]]=core #from name
    
    for i in range(len(aa)):
           temp_2_1[aa[i]]=folder[a][1][i]
    #temp_2_1['masalu_r_palm_down_30']=246
    #temp_2_1['masalu_r_palm_down_80']=555
    
    temp_3['total img']=folder[a][0]
    temp_3['count']=temp_2_1
    temp_3['files']=temp_2 
    #'temp_2# 3layers'
        
    #temp_3['count']={'masalu_r_palm_down_30':246,'masalu_r_palm_down_80':555}
    
    
    #'shell# 4layers'
    shell['Date']='2020-11-16'
    shell['Path']='D:/WinSCp/To_Do_List/white_R/'
    shell['r_palm_down/']=temp_3 #from outside folder
    
    
    output=json.dumps(shell,indent=4, sort_keys=False) #自己改
   
                                                           
    with open('C:/Users/HankWu/Desktop/outxxput.json','w') as f:
      f.write(output)

    #return shell
    
    
    
    
   
    
    