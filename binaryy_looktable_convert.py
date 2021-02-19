# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 11:18:09 2021

@author: hankwu
"""
#table form
#index_233:11101001:0xe9:0351# 重要
#(dec,binary,hexx,octt)

with open('C:/Users/HankWu/Documents/Python Scripts/QT/bits_look_table.txt','r') as f:
#with open('C:/Users/Wish/.spyder-py3/QT/bits_lookup_table.txt','r') as f:    
        gg=f.readlines()
    
'(dec,binary,hexx,octt)'
    
dec = gg[255].split(':')[0].replace('index_','')
binary = gg[255].split(':')[1]    
hexx = gg[255].split(':')[2]    
octt = gg[255].split(':')[3].replace('\n','')   
    
s=('default',dec,binary,hexx,octt)  # 重要有n 佔一位   
 
    
 
   

#y(binary,[dec,hexx,octt])  #{}
#y(hexx,[dec,hexx,octt])  #{}
#

#s=(dec,binary,hexx,octt) input
s=('default',dec,binary,hexx,octt)  # 重要有n 佔一位   

'0 >>decimal''ex 找 lookup_table2(0,*s)'
'1 >>binary''ex 找 lookup_table2(1,*s)'
'2 >>hex'
'3 >>oct'
'** lookup_table(*s) 有error**'
#s=(0,dec,binary,hexx,octt)  # 重要有n 佔一位 
def lookup_table(n,*args):
    """find correspond base value"""
    
    lis=[]
    dec=args[1]
    binary=args[2]
    hexx=args[3]
    octt=args[4] #要改
    
    lis.append(dec)
    lis.append(binary)
    lis.append(hexx)
    lis.append(octt)  #要改
    y=lambda x,y:{x:y}
    
    #y(binary,[dec,hexx,octt])  #{}
    #y(hexx,[dec,hexx,octt])  #{}
    
    #if n==int('%d'%n):
     #   lis.pop(int('%d'%n))
    lis[n]='Null'
    #lis.pop(n)    
   
    return y(args[n+1],lis)    

'0 >>decimal''ex lookup_table2(0,*s)'
'1 >>binary''ex lookup_table2(1,*s)'
'2 >>hex'
'3 >>oct'
str1=['decimal : ','binary : ','heximal : ','octal : ']

def lookup_convert(i,a,default=1): #從轉2進制轉成其他default to a #倒過來看轉換
    """convert lookup table value to selected base
       base start from 0~3 above
       b,a : base
       ex: decimal-base to binary-base
           lookup_convert(255,2) 轉16進制常用
       i : 10進制
    """
    str1=['decimal : ','binary : ','heximal : ','octal : ']
    with open('C:/Users/HankWu/Documents/Python Scripts/QT/bits_lookup_table.txt','r') as f:    
    #with open('C:/Users/Wish/.spyder/QT/bits_lookup_table.txt','r') as f:    
        gg=f.readlines()
    
    '(dec,binary,hexx,octt)'
    
    dec = gg[i].split(':')[0].replace('index_','')
    binary = gg[i].split(':')[1]    
    hexx = gg[i].split(':')[2].replace('\n','')       
    octt = gg[i].split(':')[3].replace('\n','')   
    
    s=('default',dec,binary,hexx,octt)  # 重要有n 佔一位 要改
    s#=('default',dec,binary,hexx)  # 重要有n 佔一位
    
    u=lookup_table(default,*s)
    
    if default==a:
        for x,y in u.items():
           
           print('{}{}..>> {}{}'.format(str1[default],x,str1[default],x))
           print()
           return(x)
        
    else:
        for x,y in u.items():
        
    #        print('{}{}'.format(str1[b],x)) 擇一
    #        print(y)
    #        print('{}{}'.format(str1[a],y[a]))
      
            print(y)
            print('{}{}..>> {}{}'.format(str1[default],x,str1[a],y[a]))
            print()
            
            return(y[a])
        
    
def list_of_base(default=1):
    '0 >>decimal''ex list_of_base(0)'
    '1 >>binary''ex list_of_base(1)'
    '2 >>hex'
    '3 >>oct'
    
    lis={}
    #with open('C:/Users/Wish/.spyder-py3/QT/bits_lookup_table_large - Copy.txt','r') as f:    
    with open('C:/Users/HankWu/Documents/Python Scripts/QT/bits_lookup_table_large - Copy.txt','r') as f:    
        gg=f.readlines()
    
    '(dec,binary,hexx,octt)'
    for i in range(len(gg)):
        dec = gg[i].split(':')[0].replace('index_','')
        binary = gg[i].split(':')[1]    
        hexx = gg[i].split(':')[2].replace('\n','')       
        octt = gg[i].split(':')[3].replace('\n','')   
        
        s=('default',dec,binary,hexx,octt)  # 重要有n 佔一位 要改
        #s=('default',dec,binary,hexx)  # 重要有n 佔一位
    
        u=lookup_table(default,*s)
        key=list(u.keys())
        #print(key)
        value=list(u.values())
        #print(value)
        lis[key[0]]=value[0]
    
    return lis


    
def lookup_convert_by_base(inpu,a,default=1): #input要跟進default 1>bin,2>hex
    
    str1=['decimal : ','binary : ','heximal : ','octal : ']
    
    T=list_of_base(default)
    
    u={inpu:T[inpu]}
    
    if default==a:
        for x,y in u.items():
           
           print('{}{}..>> {}{}'.format(str1[default],x,str1[default],x))
           print()
           return(x)
        
    else:
        for x,y in u.items():
        
    #        print('{}{}'.format(str1[b],x)) 擇一
    #        print(y)
    #        print('{}{}'.format(str1[a],y[a]))
      
            print(y)
            print('{}{}..>> {}{}'.format(str1[default],x,str1[a],y[a]))
            print()
            
            return(y[a])
    
    #print(T[inpu])
    
    
d='001'

s='01'

th='0001'

th.split('0',3)
    
def check_000(a): #bug
    
    #print(len(a))
    index=int
    out=a.split('0',102)
    len(out)
    for i in range(len(out)):
        if out[i]==str(1) and ''.join(out[0:i])=='' and ''.join(out[i+1:])=='' :
            index=i
            print(index)
            output=out[index:]      
            #return(''.join(out))
        elif out[i]==str(11) and ''.join(out[0:i])=='' and ''.join(out[i+1:])=='' :
            index=i
            print(index) 
            output=out[index:]      
        elif out[i]==str(111) and ''.join(out[0:i])=='' and ''.join(out[i+1:])=='' :
            index=i
            print(index)    
            output=out[index:]      
        elif out[i]==str(101) and ''.join(out[0:i])=='' and ''.join(out[i+1:])=='' :
            index=i
            print(index)    
            output=out[index:]      
    x=''        
    #output=out[index:]      
    for i in range(len(output)):
        if output[i]=='':
            output[i]=output[i].replace('','0')

        x+=output[i]
    
 #   return out[index:]
    return x

'''
check_nnn the same str(int('001001')) 1001 去零
'''    
def check_nnn(a,n=32): #切100/32次 integer
    
    index=int
    out=[]
    L=a.split('-')
    
    if len(L)>1:#'-'
            a=L[-1]
            x=str(int(a))
            
            return '-'+x
    else:  #'+'
        
        a=L[0]
        for i in range(n):
            xx=a.split('0',i)
            out.append(xx)
            #print(out)
        for i in range(len(out)):
            lis=out[i]
            for j in range(len(lis)):
                if lis[j]!=None and ''.join(lis[0:j])=='' and ''.join(lis[j+1:])=='' :
                    index=j
                    #print(index)
                    output=lis[index:]  
                    #print(output)
                        
        x=''        
        #output=out[index:]      
        for i in range(len(output)):
            if output[i]=='':
                output[i]=output[i].replace('','0')
            
            x+=output[i]
        
     #   return out[index:]
        return x         
                
def check_nnn_16_base(a):
    
    L=a.split('-')
    
    if len(L)>1:#'-'
            a=L[-1]
            a=a.replace('0x','')
            return '-0x0'+check_nnn(a)
            
    else:
        a=L[0]
        a=a.replace('0x','')
        return '0x0'+check_nnn(a)
    
def list_reverse(a):

    index_verse = [-1-x for x in range(len(a))]      
    
    lis_verse = [a[x] for x in index_verse]
    return lis_verse  
    
    
    
    
    
    
    
    
    

    
    
    
    