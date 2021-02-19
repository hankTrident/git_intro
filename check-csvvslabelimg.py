# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 17:22:03 2020

@author: hankwu
"""
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
import matplotlib.patches as patches

dir_fr='C:/Users/HankWu/Desktop/Field_test_metting_room_1/' #要改
df=pd.read_csv(dir_fr+'1000.csv') #要改
#df=pd.read_csv(dir_fr+'video2_6F_H.csv')
#col=df.head() 
#col=sorted(df)
col=list(df.columns.values)
df=df.rename(columns={col[0]:'table'})
df1=pd.DataFrame(col,columns=['table'])
df=df1.append(df,ignore_index=True) 
x=df['table']

y=glob.glob(dir_fr+'*.jpg') #對比組#image  要改
#y=glob.glob(dir_fr+'*.xml')
#y=glob.glob(dir_fr+'*.png')
x1,Qvalue,y1,x2=[],[],[],[]
for i in range(len(x)):
      oo=x[i].split(';')[0]
      #ot=x[i].split(';')[0].replace('frame1','Rpalm_1') #要改
      ox=x[i].split('.jpg')[-1]   #要改
      #ox=x[i].split('.xml')[-1]   #要改
      #ox=x[i].split('.png')[-1]
      x1.append(oo)
      #x2.append(ot)
      Qvalue.append(ox)

for i in range(len(y)):
      oy=y[i].split('\\')[-1]
      y1.append(oy)
   
tree,tree_less={},{}
if len(y1)>len(x1):
     for i in range(len(y1)):      #file more
         tree['{}'.format(y1[i])]='index{}'.format(i) #原始
         # tree['{}'.format(x2[i])]='{}'.format(Qvalue[i])
     for i in range(len(x1)):     #比對組 file less
              tree_less[x1[i]]=1
     
     tree.update(tree_less)
     
     c,c1=0,0
     
     for key, value in tree.items(): 
            
         if value==1: 
     #            print(key) 
                 c+=1
         
         else:
             pass
     print('The overlapping : %d 數量\n'%c)
     ('\n')
     for key, value in tree.items(): 
            
         if value==1: 
            pass
     
         else:
             print(key) 
             c1+=1
     print('The lose files : %d 數量'%c1)

elif len(x1)>len(y1):
     for i in range(len(x1)):      #file more
         tree['{}'.format(x1[i])]=Qvalue[i]
     for i in range(len(y1)):     #比對組 file less
              tree_less[y1[i]]=1
     
     tree.update(tree_less)
     
     c,c1=0,0
     
     for key, value in tree.items(): 
            
         if value==1: 
     #            print(key) 
                 c+=1
         
         else:
             pass
     print('The overlapping : %d 數量\n'%c)
     
     for key, value in tree.items(): 
            
         if value==1: 
            pass
     
         else:
             print(key,end=' ') 
             c1+=1
     print('The lose files : %d 數量'%c1)
else:
   
     for i in range(len(y1)):      #file more
         
          tree['{}'.format(y1[i])]='{}'.format(Qvalue[i])
     print('They are equal,The overlapping : %d 數量\n'%len(y1))

kval=list(tree.values())
we=';71;28;193;187;1;0;98;40;146;82;2;0;'
pp=[len(x)/6 for x in kval]
threshold=4
pp_n=[x<threshold for x in pp]#two labels=6~7, one label=3~3.3 往下選 
                               #three label=10
index=[]
#for i in range(len(pp)):
#    if pp[i]<threshold:
#        print(pp[i],'# %d'%i)
#         index.append(i)      
#for i in range(round(len(index)/2)):
#     if index[2*i]-index[2*i-1]>2:
#         print(index[0],index[2*i-1],index[2*i],index[-1])
#====
#tree_lis=sorted(tree.items())
#file=open('C:/Users/HankWu/Desktop/IRsubject3/Rpalm_1/out.csv','w')
#for i in range(len(tree_lis)):
#          file.write(tree_lis[i][0]+tree_lis[i][1]+'\n')
#file.close()      
#====
x_bin=list(range(len(pp)))         
#plt.plot(x_bin,pp)
plt.scatter(x_bin,pp)
#plt.stem(x_bin,pp,use_line_collection=True)
ax=plt.gca()
rect = patches.Rectangle((0,2.17), #x1,y2
                 1330,1.33,  #width ,height
                 #edgecolor='cyan',
                 linewidth=2,edgecolor='pink',fill = False,label='1')
rect1 = patches.Rectangle((0,4.17),
                 1330,2.66,
                 linewidth=2,edgecolor='yellow',fill = False,label='2')
rect2 = patches.Rectangle((0,6.17),
                 1330,4,
                 linewidth=2,edgecolor='cyan',fill = False,label='3')
                 
ax.add_patch(rect)
ax.add_patch(rect1)
ax.add_patch(rect2)
plt.legend()
plt.show()



