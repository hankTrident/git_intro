# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 13:51:24 2020

@author: hankwu
"""
import json

with open('C:/Users/HankWu/Desktop/standard.json','r') as load_f:
     load_dict = json.load(load_f)
     print(load_dict) 

'''
先寫入dict先加入 or事後排序 看json layer前頭
'''
core,temp_2,temp_3,shell={},{},{},{}
   # '1th, 2nd ,  3rd,  4th'
temp_2_1={}


core['bounding box']=[102,98,189,179]#from csv  box  
core['folder']='Huck_two_30'    #from folder[i][2]

temp_2['20201006161237135.png']=core #from name
temp_2_1['masalu_r_palm_down_30']=246
temp_2_1['masalu_r_palm_down_80']=555
#'temp_2# 2layers'


temp_3['total img']=2571
temp_3['count']=temp_2_1
temp_3['files']=temp_2 


#'temp_3# 3layers'

#temp_3['count']={'masalu_r_palm_down_30':246,'masalu_r_palm_down_80':555}

#'shell# 4layers'

shell['Date']='2020-11-16'
shell['Path']='D:/WinSCp/To_Do_List/white_R/'
shell['r_palm_down/']=temp_3 #from outside folder

    
#output=json.dumps(shell,indent=4, sort_keys=True,separators=(',', ': ')).replace('\\n','\n')
                                                            #(', ', ': ')
output=json.dumps(shell,indent=4, sort_keys=False) #自己改
                                                           
with open('C:/Users/HankWu/Desktop/outxxput.json','w') as f:
      f.write(output)




