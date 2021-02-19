import sys
import os
from math import *
from PyQt5 import QtGui,QtWidgets,QtCore
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication,QDialog,QLineEdit,QTextBrowser,QVBoxLayout
from PyQt5.QtWidgets import *

'''
Ctrl+Z 
Ctrl+V
Ctrl+C
'''
str1=[] 
#class Form(QWidget):#不適mainwindow        
#不適mainwindow
class Form(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)
        self.setWindowTitle('Notebook')
        self.setGeometry(800,100,400,600)
        self.browser = QTextBrowser()
        self.browser.setStyleSheet('background-color:#ffe6e6') #網頁

        self.dir='C:/Users/HankWu/Documents/code.txt' #要改
        self.dir2='C:/Users/HankWu/Desktop/wiki.txt'
        self.dir3='C:/Users/Wish/Desktop/code.txt'
        self.dir4='C:/Users/hunk.wu/Desktop/msn.txt'
        self.dir3='C:/www/this.html'# 不建議用
        
        self.txt_open()# 自己建立TXT 

        self.html_open()#'網頁原始碼存.txt' 



        #self.browser.setText
        #self.browser.setSource(QUrl(QUrl.fromLocalFile(dir2)),100)
        #self.browser.setSource(QUrl(QUrl.fromLocalFile(dir3)),100) #100(files) VS 1(htnl)
        
        self.browser.setOpenExternalLinks(True)
        #self.browser.setSource(QUrl('C:/www/this.html'),1)
        #self.browser.loadResource(100,QUrl('C:/Users/HankWu/Desktop/cnn.txt'))
        #self.browser.home()
        self.lineedit = QLineEdit('%s#'%'input the expression and press Enter')
        #self.lineedit = QLineEdit()
        self.lineedit.selectAll()
        self.lineedit.redo()
        self.lineedit.undo()
        #self.lineedit.
        #self.lineedit.paste()
        #==font size
        f=self.lineedit.font()  #字體
        f.setPointSize(14)        #字體大小
        f.setFamily('Arial')        #字體自型
        #f.setFamily('calibri')
        #f.setFamily('MS Shell Dlg 2')
        #f.setFamily('sans-serif')
        self.lineedit.setFont(f)

        f_1=self.browser.font() #字體
        f_1.setPointSize(14)
        f_1.setFamily('Arial')
        #f_1.setFamily('calibri')
        #f_1.setFamily('MS Shell Dlg 2')
        #f_1.setFamily('sans-serif')
        self.browser.setFont(f_1)
                 # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()
        
        #text = self.lineedit.text() #input 
        
        #self.lineedit.returnPressed.connect(self.mode)
        #simbol=['+','-','*','/','**','//','%','math','sqrt','log','+=','-=','/=','*='] 
        
        self.lineedit.returnPressed.connect(self.updateUi)
        #self.mode()
        #self.update()
        
    def html_open(self):
        
        global str1

        with open(self.dir2,'r',encoding='utf-8') as f: #可取消
        #with open(self.dir3,'r') as f:	
            uu=f.read()
        
        #self.browser.setText("<table><caption>Alien football stars</caption><tr><th scope=\"col\">Player</th><th scope=\"col\">Gloobles</th><th scope=\"col\">Za'taak</th></tr><tr><th scope=\"row\">TR-7</th><td>7</td><td>4,569</td></tr><tr><th scope=\"row\">Khiresh Odo</th><td>7</td><td>7,223</td></tr><tr><th scope=\"row\">Mia Oolong</th><td>9</td><td>6,219</td></tr></table>")
        self.browser.setText(uu)
        str1.append(uu)

    def txt_open(self):
        
        global str1
        
        
        def Url_checkfrFile(a='https'):
            
            
            urls=[]
            tupl=[]
            ind=[] # 原始第幾行

            dir2='J:/Py scripts/QT/log_calculate.txt'
            #dir2='C:/Users/hunk.wu/Desktop/log_calculate.txt'
            with open(self.dir4,'r',encoding='utf-8') as f: #可取消
                    #with open(self.dir3,'r') as f: 
                        uu=f.readlines() #list


            for i in range(len(uu)):
                
                k=uu[i].split('%s'%a)
                #print(k)
                for j in range(len(k)):
                    
                    url=k[j].split(' ')
                    for z in range(len(url)):
                        bol=url[z].find('://')!=-1 #有
                        bol2=url[z].find('.')!=-1
                        
                        t=lambda x,y,z:(x,y,z) # 是函數要有()
                        #操作
                        xx=t(bol,'%s'%a+url[z],i)[0]
                        uurl=t(bol,'%s'%a+url[z],i)[1].replace('\n','')
                        uurl_1=t(bol,url[z],i)[1][1:20]
                            
                        index=t(bol,'%s'%a+url[z],i)[2] # 原始第幾行
                        
                        if xx==True and t(bol2,url[z],z)[0]==True:
                            print(t(bol,url[z],i))
                            print()
                            urls.append(uurl)
                            tupl.append((uurl,uurl_1))
                            ind.append(index)
             
            return tupl
        #return urls
        

        def Url_checkfrBrowr(a='https'):
            
         
            urls=[]
            tupl=[]
            ind=[] # 原始第幾行
            
            #dir2='J:/Py scripts/QT/log_calculate.txt'
            #dir2='C:/Users/hunk.wu/Desktop/msn.txt'
            with open(self.dir2,'r',encoding='utf-8') as f: #可取消
                    #with open(self.dir3,'r') as f: 
                        uu=f.readlines() #list
            
            
            for i in range(len(uu)):
                
                k=uu[i].split('%s'%a)
                #print(k)
                for j in range(len(k)):
                    
                    url=k[j].split(' ')
                    #print(url)
                    for v in range(len(url)):
                        
                        xf=url[v].split('"')
                        
                        for z in range(len(xf)):
                                bol=xf[z].find('://')!=-1 #有
                                bol2=xf[z].find('.')!=-1
                                
                                t=lambda x,y,z:(x,y,z) # 是函數要有()
                                #操作
                                xx=t(bol,'%s'%a+xf[z],i)[0]
                                uurl=t(bol,'%s'%a+xf[z],i)[1].replace('\n','')
                                uurl_1=t(bol,xf[z],i)[1][1:20]
                                    
                                index=t(bol,'%s'%a+xf[z],i)[2] # 原始第幾行
                             
                                if xx==True and t(bol2,xf[z],z)[0]==True:
                                    print(t(bol,xf[z],i))
                                    print()
                                    urls.append(uurl)
                                    tupl.append((uurl,uurl_1))
                                    ind.append(index)
                     
            return tupl
            #return urls

        def Url_check_repeat(a):
            
            vs={}
            for i in range(len(a)):
                vs[a[i]]=i
            
            #for key,value in vs.items():
            
            return list(vs.keys())
            ' url=Url_check_repeat(url)'



        #urls=Url_checkfrFile()
        urls=Url_checkfrBrowr('http')

        url=[]
        reps=[]
        for i in range(len(urls)):
     
             reps.append('<a href=\"{}\">{}</a><img src=\"4e7_{}.jpg\">'.format(urls[i][0],urls[i][1],i+1))#\" \" 重要
             url.append(urls[i][0])
        #print('<a href=\\"{}\\">{}</a><img src=\\"4e7_{}.jpg\\">'.format(urls[i][0],urls[i][1],i+1)+'\n')
        
     
         #"<a href=\"{}\"></a><img src=\"4e7_6.jpg\">"  #\" \" 重要          
                                              #直接輸入不用\" <a href="https:
                                             # export \" 消失了 <a href="https:
                                             #  want export <a href=\"https:  \\"  \\"
        with open(self.dir2,'r',encoding='utf-8') as f: #可取消
        #with open(self.dir3,'r') as f:	
            uu=f.read() #list
        
        #url=url[:10]
        #reps=reps[:10]
        for x,y in zip(url,reps):  #家zip 多次replace in one file multi 'str'
    
            uu=uu.replace(x,y)

            print(uu)
       
        self.browser.setText(uu)
        #self.browser.setText(uu.replace('<html lang',''))


        #self.browser.setText("<a href=\"https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-8.noarch.rpm\">//download1.rpmfusi</a><img src=\"4e7_6.jpg\">")
        #self.browser.setHtml()
        str1.append(uu)

        
        with open(os.getcwd()+'/final.txt','w',encoding='utf-8') as f:
               f.write(uu)
            
        #print(QStandardPaths.displayName(0)) #0:desktop ,1:document
        #print(QStandardPaths.locate(0,'code.txt')) #找
        #print(QStandardPaths.locateAll(1,'.csv')) #找            

    def mode(self): #not use
        
        text = self.lineedit.text() #input 
        
        print(text)
        #text='input the expression and press Enter'        
        def compar(a):
            s=[]
            simbol=['+','-','*','/','**','//','%','math','sqrt','log','+=','-=','/=','*=']
            for i in range(len(simbol)):
                if a.find(simbol[i])!=-1:
                   s.append(a)
        
                   
                else:
                    pass
               
            if len(s)!=0:
                return s[0]
            else:  #沒有
                return -1
            
       
 
        if compar(text)==-1:
            self.lineedit.returnPressed.connect(self.updateUi_text)
            print(compar(text))
        else:
            self.lineedit.returnPressed.connect(self.updateUi)
            print('+')
        
            
    def updateUi_text(self):

        global str1
        
        text=self.lineedit.text()#input
        self.browser.append('%s'%(text)) #文字 str
        str1.append('{}'.format(text))
        print(str1)
        self.save()# 可取消
        self.lineedit.clear()# 可取消
        

    def updateUi(self):
        
        global str1
        import math
        
        text = self.lineedit.text()
        
        def compar(a):
            s=[]
            simbol=['+','-','*','/','**','//','%','math','sqrt','log','+=','-=','/=','*=']
            for i in range(len(simbol)):
                if a.find(simbol[i])!=-1:
                   s.append(a)
        
                   
                else:
                    pass
               
            if len(s)!=0:
                return s[0]
            else:  #沒有
                return -1
        
        if  compar(text)!=-1: #有+
#           
            try:
                
                text = self.lineedit.text()#input
                
                result = eval(text)
            
            	#print(text,result)
                self.browser.append('%s = %s' %(text,result)) #變計算機
            	#str1.append('%s = %s' %(text,result))
                str1.append('{} = {}'.format(text,result)) #the same
                print(str1)  
                self.save()# 可取消
                self.lineedit.clear()# 可取消
                
              
            except:
                
                
                self.browser.append('<font color=red>%s is invalid!</font>' %text)
               
                self.lineedit.clear()
                
        else: #沒有+
            self.updateUi_text()
            self.lineedit.clear()
            
            
    def save(self):
        global str1

        with open(os.getcwd()+'/log_calculate.txt','w',encoding='utf-8') as f: #重要 存簡體字改 utf-8**
        	
            for x in enumerate(str1):#len append 數量
                #print(x[1])
                f.write(x[1]+'\n')

    def button(self):

        self.lineedit.setText('The number you selected: Space')
        #self.bt=QtGui.KeyPress()
        #self.bt.QInputEvent('UP')
        #print(bool())

#    def eventFilter(self, source, event): #不同數字 鍵盤事件
#        if (event.type() == QEvent.KeyPress and source is self.lineedit):
#            print('key press:', (event.key(), event.text()))
#        return super(Form, self).eventFilter(source, event)
     
        

    def showCurrentText(self, text):

        print('current-text:', text)

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()