# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 22:30:03 2021

@author: Wish
"""
from binaryy_looktable_convert import *
import numpy as np

'integer'  
x=9992 #down to up
#x=555521 #down to up
indice=[]
index_hex=[str(x) for x in range(10)]+['a','b','c','d','e','f']
index=[str(x) for x in range(16)]
index_bin=['0000','0001','0010','0011','0100','0101','0110','0111','1000',
           '1001','1010','1011','1100','1101','1110','1111']

for i in range(100):
    x/=16
    print('{}, {}'.format(int(x),(x-int(x))*16))
#    integr=int(x)
#    flot=(x-int(x))*16
#    indice.append(int(flot)) #取餘數
#    
#    if flot==0:#重要
#        continue
#    
#    elif flot<0.1 and integr==0:#重要
#        break
#    
#    else:
#        continue

# =============================================================================
    
    integr=(x-int(x))*16
    indice.append(int(integr)) #取餘數
    
    if integr==0:#重要
        continue
    
    elif integr<0.1 and int(x)==0:#重要
        break
    
    else:
        continue  
# =============================================================================
indice=list_reverse(indice)
indice=[str(x) for x in indice]

print(indice)
table,table_hex={},{}
y=lambda x,y:{x:y}
for i in range(len(index)):
    table[index[i]]=index_bin[i]
#print(table)
for i in range(len(index_hex)):
    table_hex[index[i]]=index_hex[i]
    
u,w='','0x'
for i in range(len(indice)):#u 鋪平[1,0]sequential list
    
       u+=table[indice[i]]
       w+=table_hex[indice[i]]      

b=check_nnn(u,100) #去零
a=check_nnn_16_base(w)
print()
print(b)
print(a)
#    
#'float'
#y=235/256
#y=0.625      # up to down
#for i in range(3):
###    y*=16
##    print('{}, {}'.format(int(y),(y-int(y))*16))
#    y*=2
#    print('{}, {}'.format(int(y),(y-int(y))*2))
    

#recusive f not yet
#def suply_000(n): #不藥用
#    
#    if len(n)%4==0:
#        pass
#        return(n)
#    else:
#        if len(n)%4==3:
#            N='0'+n
#            return(N)
#        elif len(n)%4==2:
#            N='00'+n
#            return(N)
#        elif len(n)%4==1:
#            N='000'+n
#            return(N)

def suply_000(n,a=4):#4各一組chop'0000'
    
     if len(n)%a==0:
        
        #st='0'*4 #set bits counts
        st='0'*a  
        N='0'*(len(st)-len(n))+n
        return(N)         
     else:
         
         b=(len(n)//a+1)*a 
         st='0'*b  
         N='0'*(len(st)-len(n))+n
         return(N)         

#index=[str(x) for x in range(10)]+['a','b','c','d','e','f']
#index_bin=['0000','0001','0010','0011','0100','0101','0110','0111','1000',
#           '1001','1010','1011','1100','1101','1110','1111']
   
#y=list(zip(index,index_bin))        

n='1110001001011001'

def bin_to_hex(n):
    
    index=[str(x) for x in range(10)]+['a','b','c','d','e','f']
    index_bin=['0000','0001','0010','0011','0100','0101','0110','0111','1000',
           '1001','1010','1011','1100','1101','1110','1111']
    
    n=suply_000(n)        
    
    bin=[n[0+4*x:4+4*x] for x in range(len(n)//4)]
    
    for i in range(len(bin)): #input ['0000'] to ['a']
      for x,y in zip(index_bin,index):
        
            bin[i]=bin[i].replace(x,y)
      #print(bin[i])
      #print()
      
    #print(bin)
    
    a='0x'
    for i in range(len(bin)):
        a+=bin[i]
    print("binay : '{}' , hex : '{}'".format(n,a))

def list_reverse(a):

    index_verse = [-1-x for x in range(len(a))]      
    
    lis_verse = [a[x] for x in index_verse]
    return lis_verse
       
n='1110001001011001'
#n='1111000101111111'

def bin_to_decimal(n,a=32):#a=1 error
    """
    convert to dec by base cal
    a : base 
    """
    u=[]
    bit=check_nnn(n)
    n=suply_000(n,a)        
        
    bin=[n[0+4*x:4+4*x] for x in range(len(n)//4)]
    #print(bin)
    for i in range(len(bin)):#u 鋪平[1,0]sequential list
       t=[int(x) for x in list((bin[i]))]    
       u+=t       
        
    y=np.array(u)
    ty=np.reshape(y,(int(len(u)/a),a)) # integer input# 16/8/4一組
    print(ty) 
    row,col=ty.shape
    
    lis1=[(2)**x for x in range(col)] #create(16,1)#要反轉
    lis1=list_reverse(lis1)
    io=np.array(lis1)
    io=np.reshape(io,(col,1))
    
#    io=np.array([[2**15],[2**14],[2**13],[2**12],[2**11],[1024],[512],[256]
#    ,[128],[64],[32],[16],[8],[4],[2],[1]])
    out=np.dot(ty,io) 
    #print(io)    #8/32/64/128 #64怪怪der
    #print(out)
    
    #lis=[256**x for x in range(row)]
    lis=[(2**a)**x for x in range(row)]  #create(1,16)#要反轉
    lis=list_reverse(lis)
    base_32=np.array(lis)   #8/32/128(快)
# =============================================================================
    #base_162=np.array(list_reverse(lis))
    decimal=(np.dot(base_32,out))
    print("binay : '{}' , dec : '{}'".format(n,decimal[0]))
    print('%d.bits'%(len(bit)))
    return(decimal[0])
        
        

        
        
        
        
        
        
        
        
        
        
        
