# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 20:30:46 2020

@author: Wish
"""
import sys
from PyQt5 import QtGui,QtWidgets,QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import *
import os
import json
#import pandas as pd
#import glob
from PIL import ImageQt

from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from pyquery import PyQuery as pq
import time   


lis1=[]
dir_choose=str
num=0
csv_map={}


'''
class SubWidget(QtWidgets.QWidget):# not yet
    def __init__(self):
        super(SubWidget,self).__init__()
        self.label_2 = QtWidgets.QLabel("Label 2",self)
        img = QtGui.QPixmap("C:/Users/HankWu/Documents/Python Scripts/Mario.gif")
        

        self.label_2.setPixmap(img) #將 image 加入 label 顯示誰~~
'''     

class MyLabel(QtWidgets.QLabel):
      def __init__(self,event):
        super(MyLabel,self).__init__(event)# **event**
        #super().__init__(event)#
       # super(Window,self).__init__()
        self.x0=0
        self.y0=0
        self.x1=0
        self.y1=0 
        #self.img=QtGui.QLabl.QPixmap()
        #self.img=QtWidgets.QLabel('FIG.',self)
        flag=False
     

      def mousePressEvent(self,event):
        #super(QGraphicsView, self).paintEvent(event)
        self.flag=True
        #self.x0=event.pos.x()
        #self.y0=event.pos.y()
        self.x0=event.x()
        self.y0=event.y()
        
      
      def mouseReleaseEvent(self,event):
        #super(QGraphicsView, self).paintEvent(event)
        self.flag=False

      def mouseMoveEvent(self,event):
        #super(QGraphicsView, self).paintEvent(event)
        if self.flag:
              self.x1=event.x()    
              self.y1=event.y()
              self.update()
    
      def paintEvent(self,event):
            global lis1
            global num
            global dir_choose
            global csv_map

            if len(lis1)<=0:
               pass
            else:#super(QGraphicsView, self).paintEvent(event)
                super().paintEvent(event)
                if self.x1<self.x0:
                    rect=QtCore.QRect(self.x1,self.y1,abs(self.x1-self.x0),abs(self.y1-self.y0))        
                elif self.y1<self.y0:
                    rect=QtCore.QRect(self.x1,self.y1,abs(self.x1-self.x0),abs(self.y1-self.y0))            
                else:
                    rect=QtCore.QRect(self.x0,self.y0,abs(self.x1-self.x0),abs(self.y1-self.y0)) 

                img=QtGui.QPixmap(lis1[(num%len(lis1))])      
                #self.img.setPixmap(img)  
                self.painter=QtGui.QPainter(img)
                self.pen=QtGui.QPen(QtCore.Qt.red)
                self.pen.setWidth(2)
                self.painter.setPen(self.pen)
                
                self.painter.drawRect(rect)
                self.painter.end()
                self.setPixmap(img)  
                   #self.updateImage_lb(lis1[(num%len(lis1))])
'''
      def updateImage_lb(self,imageName): #回傳imageName
           img=QtGui.QPixmap(imageName)
           #self.label.setPixmap(img)
           self.lb.setPixmap(img)            
'''


class Window(QtWidgets.QMainWindow):
   # global lis1
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50,50,650,472) #主視窗 加了label.lb 視窗變大
        
        self.setWindowTitle('Pyqt5 Tuts!')
        self.setWindowIcon(QtGui.QIcon('20200608_000813.jpg'))
        self.statusBar().showMessage('currnet state bar, 500')
        
        self.main_widget = QtWidgets.QWidget(self)
        #self.sub_widget= SubWidget() 

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.setMouseTracking(True)
        self.lb = MyLabel(self)
        #self.lb.setGeometry(QRect(30, 30, 311, 241))
        self.lb.setCursor(Qt.CrossCursor)

        #*****important
        
#        layoutGrid=QtWidgets.QGridLayout()
#        self.setLayout(layoutGrid)
        l_h = QtWidgets.QHBoxLayout(self.main_widget)# 重要
        
#        grid = QtWidgets.QGridLayout()
#        grid.setColumnMinimumWidth(1,50)
        g_h = QtWidgets.QHBoxLayout() #QV_Box vs QH_Box
        p_h = QtWidgets.QHBoxLayout() #QV_Box vs QH_Box
        x_v = QtWidgets.QVBoxLayout() 
        z_v = QtWidgets.QVBoxLayout()
        j_v = QtWidgets.QVBoxLayout()
        y_v = QtWidgets.QVBoxLayout()
        w_v = QtWidgets.QVBoxLayout() #QV_Box vs QH_Box
        
        self.groupBox = QtWidgets.QGroupBox('FIG.',self)
        #self.groupBox.setGeometry(QtCore.QRect(5, 65, 430, 321))
        self.groupBox.setObjectName("groupBox")
        #self.groupBox.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        
        self.groupBox_2 = QtWidgets.QGroupBox('ToolBar',self)
        #self.groupBox_2.setGeometry(QtCore.QRect(5, 390, 430, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setMinimumHeight(61)
        
        
        self.groupBox_3 = QtWidgets.QGroupBox('Display Window',self)
        #self.groupBox_3.setGeometry(QtCore.QRect(450, 65, 191, 401))
        #self.groupBox_3.setMinimumWidth(191)
        self.groupBox_3.setMaximumWidth(191)
        self.groupBox_3.setObjectName("groupBox_3")
        
        self.groupBox_4 = QtWidgets.QGroupBox(self)
        self.groupBox_4.setMinimumHeight(120)
        self.groupBox_4.setMinimumWidth(191)
        #self.groupBox.setGeometry(QtCore.QRect(5, 65, 430, 321))
        self.groupBox_4.setObjectName("groupBox_4")
        
        btn=QtWidgets.QPushButton('Quit',self)
        
        #btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.clicked.connect(self.close_main_application)
        btn.resize(90,30)#button size
        #btn.resize(btn.sizeHint())
        #btn.resize(btn.minimumSizeHint())
        btn.move(460,380)

        btn2=QtWidgets.QPushButton('Draw',self)
        btn2.clicked.connect(self.Process_open)
        #btn2.clicked.connect(self.brower)
        #btn2.clicked.connect(self.upDateImageAnd_draw)
        #btn2.clicked.connect(self.draw_box)

        btn2.resize(90,30)
        btn2.move(460,300)

        btn3=QtWidgets.QPushButton('Save',self)
        btn3.clicked.connect(self.draw_pic_save)
        #btn3.clicked.connect(self.upDateImageAnd_draw)
        btn3.resize(90,30)
        btn3.move(460,350)

        
        self.styleChoice=QtWidgets.QLabel(self)
        
        comboBox=QtWidgets.QComboBox(self)
        comboBox.addItem('Motif')
        comboBox.addItem('Windows')# 不能改
        comboBox.addItem('Fedora')
        comboBox.addItem('Plastique')
        comboBox.addItem('Cleanlooks')
        comboBox.addItem('Windowsvista')# 不能改
        
        #comboBox.move(460,425)
        #self.styleChoice.move(560,425)
        comboBox.activated[str].connect(self.style_choice)
        
        #self.label = QtWidgets.QLabel('FIG.',self)

        #img = QtGui.QPixmap(imageName)
        #img = QtGui.QPixmap("C:/Users/HankWu/Documents/Python Scripts/Mario.gif")
        #img = QtGui.QPixmap("C:/Users/Wish/.spyder-py3/Mario.gif")

        #self.label.setPixmap(img) #將 image 加入 label 顯示誰~~
        #self.lb.setPixmap(img)
        
        #self.label.setGeometry(12,81,415,297) # 大小
        #self.label.move(12,81)
        #self.im.scaled(200,150,aspectMode=Qt.KeepAspectRatio,mode=Qt.FastTransformation))

        #self.label.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        #self.label.setScaledContents(True)
        self.lb.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        self.lb.setScaledContents(True)
        
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self)
        self.commandLinkButton.setMaximumWidth(50)
        self.commandLinkButton.setShortcut('A')#後退
        self.commandLinkButton.clicked.connect(self.before_pic)
        self.commandLinkButton.setObjectName("commandLinkButton")
        
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self)
        self.commandLinkButton_2.setMaximumWidth(50)
        self.commandLinkButton_2.setShortcut('D')#前進
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.commandLinkButton_2.clicked.connect(self.next_pic)
        
        self.horizontalSlider = QtWidgets.QSlider(self)
        #self.horizontalSlider.setGeometry(QtCore.QRect(10, 350, 201, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        #self.horizontalSlider.setTickInterval(1)
        #self.horizontalSlider.sliderPressed(self.bar_value_change)
        self.horizontalSlider.setMaximum(20)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setValue(0)
        self.horizontalSlider.setRange(0,20)
        self.horizontalSlider.valueChanged.connect(self.bar_value_change)
        
        
        self.tabWidget = QtWidgets.QTabWidget(self)
        #self.tabWidget.setGeometry(QtCore.QRect(380, 30, 171, 251))
        self.tabWidget.setObjectName("tabWidget")
        #self.tab1 = Tab1()
        self.tab1 =QtWidgets.QWidget(self)
        self.tab2 =QtWidgets.QWidget(self)
        self.tab1.setObjectName("tab1")
        self.tab2.setObjectName("tab2")
        self.tabWidget.addTab(self.tab1, "Tab1")
        self.tabWidget.addTab(self.tab2, "Tab2")
        self.tab1UI()

#
#        self.edit=QtWidgets.QLineEdit('',self)
#        self.edit.setDragEnabled(True)
#        self.edit.move(500,50)
#
#        btn_2=Button('button',self)
#        btn_2.move(190,50)





        #self.tab2UI()
##        self.keySequenceEdit = QtWidgets.QKeySequenceEdit(self)
##        self.keySequenceEdit.setGeometry(QtCore.QRect(170, 380, 41, 21))
#        self.keySequenceEdit.setMaximumWidth(50)
#        self.keySequenceEdit.setObjectName("keySequenceEdit")
        
        gt=QtWidgets.QAction('Exit !! ',self) 
        gt.triggered.connect(self.next_pic)

        self.xx= QtWidgets.QLineEdit(self)
#        self.keySequenceEdit.setGeometry(QtCore.QRect(170, 380, 41, 21))
        self.xx.setMaximumWidth(50)
        self.xx.addAction(gt)
        self.xx.setObjectName("QLineEdit")
        #======看上面=======================
        #j_v.addWidget(self.label)
        j_v.addWidget(self.lb)
        #j_v.addWidget(self.sub_widget)
        self.groupBox.setLayout(j_v)
        
        p_h.addWidget(self.commandLinkButton)
        p_h.addWidget(self.horizontalSlider)
        p_h.addWidget(self.xx)
        p_h.addWidget(self.commandLinkButton_2)
        #p_h.addStretch(1)
        self.groupBox_2.setLayout(p_h)
        
        y_v.addWidget(self.tabWidget)
        self.groupBox_3.setLayout(y_v)
        #self.groupBox.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        w_v.addWidget(btn2)
        w_v.addWidget(btn3)
        w_v.addWidget(comboBox)
        w_v.addWidget(btn)
        #w_v.addWidget(g_h)

        self.groupBox_4.setLayout(w_v)
        
        x_v.addWidget(self.groupBox)
        x_v.addWidget(self.groupBox_2)
        
        z_v.addWidget(self.groupBox_3)
        z_v.addWidget(self.groupBox_4)
        
        l_h.addLayout(x_v)
        l_h.addLayout(z_v)

        
        extractAction=QtWidgets.QAction('Exit !! ',self)
        extractAction.setShortcut('Q')
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_main_application)
        self.statusBar()
        #*****
        
        openEditor = QtWidgets.QAction('&Editor',self)
        openEditor.setShortcut('Ctrl+E')
        openEditor.setStatusTip('Open Editor')
        openEditor.triggered.connect(self.editor)
        
        openFile = QtWidgets.QAction('&Open',self)
        openFile.setShortcut('Alt+W')
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.pic_open)
        
        saveFile = QtWidgets.QAction('&Save',self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)
        
        save_asFile = QtWidgets.QAction('&Save As',self)
        save_asFile.setShortcut('Ctrl+Shift+S')
        save_asFile.setStatusTip('Save as File')
        save_asFile.triggered.connect(self.file_save_as)

        view_csv = QtWidgets.QAction('&load CSV',self)
        view_csv.setShortcut('Alt+D')
        view_csv.setStatusTip('Load CSV...etc File')
        view_csv.triggered.connect(self.csvMap)
        
        
        mainMenu=self.menuBar()##
        #===============
        fileMenu=mainMenu.addMenu('&File')# save open menu
        
        fileMenu.addAction(openFile) #往上看
        fileMenu.addAction(saveFile)
        fileMenu.addAction(save_asFile)
        fileMenu.addAction(extractAction) #往上看
    
        editMenu=mainMenu.addMenu('&Edit')
        editMenu.addAction(openEditor)#往上看

        viewMenu=mainMenu.addMenu('&View')
        viewMenu.addAction(view_csv)#往上看
                
        editorMenu=mainMenu.addMenu('&Editor')
        editorMenu.addAction(openEditor)#往上看
       
        #self.show()
        self.home()
        
    def home(self):
        
        
        extractAction=QtWidgets.QAction(QtGui.QIcon('dog.jpg'),'Flee the Scene',self)
        extractAction.triggered.connect(self.close_application)
        self.toolBar=self.addToolBar('Extraction')
        self.toolBar.addAction(extractAction)
        
        
        fontChoice=QtWidgets.QAction('Font',self)
        fontChoice.triggered.connect(self.font_Choice)
        #self.toolBar=self.addToolBar('Font')
        self.toolBar.addAction(fontChoice)
        
        #color=QtGui.QColor(0,1,0)
        fontColor=QtWidgets.QAction('Font Bg Color',self)
        fontColor.triggered.connect(self.color_picker)
        self.toolBar.addAction(fontColor)
        
        
        checkBox=QtWidgets.QCheckBox('Enlarge Window',self)
        checkBox.move(250,30)#size
        #checkBox.toggle()#打勾勾
        checkBox.stateChanged.connect(self.enlarge_window)
        
#       
#        self.progress=QtWidgets.QProgressBar(self)
#        self.progress.setGeometry(0,300,500,20)
        
#        self.btn=QtWidgets.QPushButton('Download',self)
#        self.btn.move(300,250)
#        self.btn.clicked.connect(self.download)
        
        #print(self.style().objectName())

#        cal=QtWidgets.QCalendarWidget(self)#
        #=====日隸
#        cal.move(500,200)
#        cal.resize(200,200)
        
      
        self.show()
        
     #看def self第一行
    def Process_open(self):#qt 桌面程式打開

        folder = 'C:/www/3/vid/'
        dir = 'C:/www/3/vid/MVideo_20200924_151510_3.png'
        dir2 = 'C:/Users/HankWu/Downloads/izhik1011.avi'
        dir3 = 'C:/Users/HankWu/Downloads/cookbook.pdf'
        QDesktopServices.openUrl(QUrl(dir3))
        print(dir2)




    def brower(self):
        url='https://www.google.com'
        url2='http://localhost:8081/3/vid/pv.php'
        urls=[]
        #======
        #html=pq(url)
        #chop = webdriver.ChromeOptions()
        #chop.add_extension('C:/Users/HankWu/Documents/Python Scripts/CRX/extension_0_1_0_0.crx')
        #chop.add_extension('C:/Users/HankWu/Documents/Python Scripts/CRX/adblock.crx')
        #driver = webdriver.Chrome('C:/Users/HankWu/chromedriver/chromedriver.exe',chrome_options = chop)
        #加入絕對路徑
        ##driver = webdriver.Chrome()
        #driver.get(url)
        #time.sleep(5)
        #====
        QDesktopServices.openUrl(QUrl(url))

   
    def csvMap(self): #generate csv-map
        global csv_map
        
        fileName,filetype=QtWidgets.QFileDialog.getOpenFileName(self,'Open files','C:/Users/HankWu/Desktop/huck1014/huck-JPEGImages_part1(/','csv Files(*.csv);;xml Files(*.xml);;json Files(*.json);;All Files (*)')
        #fileName,filetype=QtWidgets.QFileDialog.getOpenFileName(self,'Open files','C:/www/3/','csv Files(*.csv);;xml Files(*.xml);;json Files(*.json);;All Files (*)')
        #=======
        #dir_fr=fileName
        #df=pd.read_csv(fileName)
        #col=list(df.columns.values)
        #df=df.rename(columns={col[0]:'table'})
        #df1=pd.DataFrame(col,columns=['table'])
        #df=df1.append(df,ignore_index=True)
        #k=df['table']
        #print('k: ',k[0],k[1])
        #========

 #       csv_map={'C:/www/3/vid8/Hank_30_R_c_thumb_2_0019.png':(2,2,30,30),
#        'C:/www/3/vid8/Hank_30_R_c_thumb_2_0020.png':(5,2,40,40),
  #      'C:/www/3/vid8/Hank_30_R_c_thumb_2_0021.png':(3,3,50,50)}
        file=open(fileName,'r')
        #print(fileName)
        with file:
           text=file.readlines()
           #text=file.read()
           csv_map={}
           csv_map_name={}#同上

           csv_map_tric=lambda x,y,index:{x:index} #output [,],{:},(,),形式跟者變 
           csv_map_tric=lambda x,y,index:[x,y,index] #callable
           j=fileName.split('/')[-1]#變path

           for i in range(len(text)):
                
                name = text[i].split(';')[0]#變path
                
                name = fileName.replace(j,'')+name #變path
               # x1 = text[i].split('.png;')[-1].split(';')[0]  #x1
                #y1 = text[i].split('.png;')[-1].split(';')[1]  #y1
                #x2 = text[i].split('.png;')[-1].split(';')[2]  #x2
               # y2 = text[i].split('.png;')[-1].split(';')[3]  #y2
                x1 = text[i].split('.jpg;')[-1].split(';')[0]  #x1
                y1 = text[i].split('.jpg;')[-1].split(';')[1]  #y1
                x2 = text[i].split('.jpg;')[-1].split(';')[2]  #x2
                y2 = text[i].split('.jpg;')[-1].split(';')[3]  #y2
                csv_map_tric(name,(x1,y1,x2,y2),i)
                key = csv_map_tric(name,(x1,y1,x2,y2),i)[0]
                value = csv_map_tric(name,(x1,y1,x2,y2),i)[1]
                index = csv_map_tric(name,(x1,y1,x2,y2),i)[2]
                csv_map[key] = value
                #===========================
                name = text[i].split(';')[0]
                csv_map_tric(name,(x1,y1,x2,y2),i)
                key = csv_map_tric(name,(x1,y1,x2,y2),i)[0]
                value = csv_map_tric(name,(x1,y1,x2,y2),i)[1]
                csv_map_name[key] = value
           #csv_map2('gf',1)
           #print('app : \n',text[0],text[1])
           #for key, value in csv_map.items():
            #print(key,value)
           
           json_map=json.dumps(csv_map_name,indent=4)    
           path=fileName.replace('.csv','.json')
           #with open(path,'w') as f:
           #   f.write(json_map)
           
        #print(text[0])
        



      


#    def JJson():


    def upDateImageAnd_draw(self):
         global lis1
         global num
         global dir_choose
         global csv_map

         #super().__init__(self)
         #csv_map={'C:/www/3/vid8/Hank_30_R_c_thumb_2_0019.png':(2,2,30,30),
         #'C:/www/3/vid8/Hank_30_R_c_thumb_2_0020.png':(5,2,40,40),
         #'C:/www/3/vid8/Hank_30_R_c_thumb_2_0021.png':(3,3,50,50)}
        #self.label.setPixmap(img)
         #img=QtGui.QPixmap("C:/Users/HankWu/Documents/Python Scripts/Mario.gif")
         img=QtGui.QPixmap(lis1[(num%len(lis1))])  

         self.penRectangle=QtGui.QPen(QtCore.Qt.red)
         self.penRectangle.setWidth(2)

         self.painterInstance=QtGui.QPainter(img)         
         self.painterInstance.setPen(self.penRectangle)
         s=csv_map[lis1[(num%len(lis1))]]
         self.painterInstance.drawRect(int(s[0]),int(s[1]),int(s[2])-int(s[0]),int(s[3])-int(s[1]))# str>int
         #不適(x1,y1,x2,y2) 是(x1,y1,x2-x1,y2-y1)
         self.painterInstance.end() #**重要
         #self.label.setPixmap(img)
         self.lb.setPixmap(img)
       
    def draw_pic_save(self):# 回傳img
        global num
        global lis1
        global dir_choose
        
        #super(MyLabel,self).__init__(self,img)
        #img=ImageQt.fromqpixmap(self.label.pixmap())#**
        img=ImageQt.fromqpixmap(self.lb.pixmap())#**

        name=lis1[(num%len(lis1))].split('/')[-1]#路徑
        
        img.save(dir_choose+name)
        print(name)
    
    
    def draw_box(self):
         global lis1
         global num
         global dir_choose

        #self.label.setPixmap(img)
         #img=QtGui.QPixmap("C:/Users/HankWu/Documents/Python Scripts/Mario.gif")
         #==
         self.lb=MyLabel(self)
         img=QtGui.QPixmap(lis1[(num%len(lis1))])  
         self.penRectangle=QtGui.QPen(QtCore.Qt.red)
         #self.penRectangle.setWidth(2)#line
         self.penRectangle.setWidth(3)#line

         self.painterInstance=QtGui.QPainter(img)         
         self.painterInstance.setPen(self.penRectangle)
         #self.painterInstance.drawRect(2,2,50,50) #不適(x1,y1,x2,y2) 是(x1,y1,x2-x1,y2-y1)
         self.painterInstance.drawPoint(50,50)
         self.painterInstance.drawPoint(10,10)
         self.painterInstance.end() #**重要

         #self.label.setPixmap(img)
         self.lb.setPixmap(img)
         #==
         #self.draw_pic_save(img)
         
         #name,type=QtWidgets.QFileDialog.getSaveFileName(self,'Save File',os.getcwd(),'All Files (*);;jpg Files (*.jpg);;png Files (*.png)')
         #img.save('C:/Users/Wish/Pictures/'+lis1[(num%len(lis1))]) 錯的
         
         
    def bar_value_change(self):
        global lis1
        global num
        
        if num==int:
           pass 
        else:
                self.horizontalSlider.setRange(0,len(lis1)-1) # 季的減一 
                num=self.horizontalSlider.value()
                self.updateImage(lis1[(num%len(lis1))])
                #print(self.horizontalSlider.value(),len(lis1))
                size=self.horizontalSlider.value()#font size
                
                #self.upDateImageAnd_draw()
        
    def next_pic(self):
        global num
        global lis1

        #if num ==0: 
        if num ==int:    
            pass
        else:
            if self.horizontalSlider.value()!=int:  #上下兩者不一樣重要
            #if num2==int:                            
               #print('+')
              
             #QCoreApplication.processEvents(self)
               num+=1
               self.updateImage(lis1[(num%len(lis1))])#括號有差
               #self.draw_box()
               #num2+=1
               #self.updateImage(lis1[(num2%len(lis1))]) #重要
             #print(num)
       # self.updateImage(self,imageName)
    def before_pic(self):
        global num
        global lis1

        if num ==int:
            pass
        else:
             if self.horizontalSlider.value()!=int:  #重要
                #print('-')
                #num2-=1
                #self.updateImage(lis1[(num2%len(lis1))]) #重要循環重複
                #QCoreApplication.processEvents(self)
                num-=1
                self.updateImage(lis1[(num%len(lis1))])   
            # print(num)
    def pic_open(self):#
        global lis1
        global num
        global dir_choose
        
        lis1=[]

        if type(dir_choose) == str :
            pass
        else:
            dir_choose = QtWidgets.QFileDialog.getExistingDirectory(self,'Working Directory',os.getcwd())
            dir_choose=dir_choose+os.sep
            print(dir_choose)

        imageName,filetype=QtWidgets.QFileDialog.getOpenFileNames(self,'Open files','C:/Users/HankWu/Desktop/huck1014/huck-JPEGImages_part1(/','png Files(*.png);;jpg Files(*.jpg);;jpg Files(*.jpeg);;All Files (*)')
        #imageName,filetype=QtWidgets.QFileDialog.getOpenFileNames(self,'Open files','C:/www/3/','png Files(*.png);;jpg Files(*.jpg);;All Files (*)')

        imageName#list domain
        if len(imageName)>0:
             for i in range(len(imageName)):
                lis1.append(imageName[i])       
                self.updateImage(imageName[0])
                #print(imageName[i])
             self.tab1UI()
             self.bar_value_change
             self.horizontalSlider.setRange(0,len(lis1)-1) # 季的減一
            #self.csvMap()
        else:
             self.bar_value_change
             self.horizontalSlider.setRange(0,len(lis1)-1) # 季的減一
         #要確認 Lena.png 路徑
        
        
        #print(filetype)
        
    def updateImage(self,imageName): #回傳imageName
#        if len(imageName)>0:
#            for i in range(len(imageName)):
#        
        img=QtGui.QPixmap(imageName)
        #self.label.setPixmap(img)
        self.lb.setPixmap(img)

    





        
    def file_open(self):
        
        fileName_choose,filetype=QtWidgets.QFileDialog.getOpenFileName(self,'Open File',os.getcwd(),"All Files (*);;Text Files (*.txt);;jpg Files (*.jpg)")
        #folder=QtWidgets.QFileDialog.getExistingDirectory(self,'Open File',os.getcwd(),)
        #print(folder)
        file=open(fileName_choose,'r')
        self.editor()
        with file:
            text=file.read()
            
            self.textEdit.setText(text)
    
    def tab1UI(self):
        global lis1
#        
        #self.xlabel=QtWidgets.QLabel(self)
        Flayout = QtWidgets.QFormLayout(self)
        widget = QtWidgets.QWidget(self)
#        for i in range(len(lis1)):
#
#             Flayout.addRow('dir',QtWidgets.QLabel('{}'.format(lis1[i]),self))
              #print(i)
               
        Flayout.addRow('dir',QtWidgets.QLineEdit())
        Flayout.addRow("地址", QtWidgets.QLineEdit())
        
        groupBox = QtWidgets.QGroupBox(self)
           
        #self.label.setPixmap(img)
        
        groupBox.setLayout(Flayout)
        scroll = QtWidgets.QScrollArea(self)
        #scroll.setWidget(widget )
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        
        
#        #为这个tab命名显示出来，第一个参数是哪个标签，第二个参数是标签的名字
#        self.tab1.setLayout(layout)
    
        f = QtWidgets.QVBoxLayout()
        f.addWidget(scroll)
        self.tab1.setLayout(f)
    
    def file_save(self):
        
        name,type=QtWidgets.QFileDialog.getSaveFileName(self,'Save File',os.getcwd(),'All Files (*);;Text Files (*.txt)')
        file=open(name,'w')
        text=self.textEdit.toPlainText()
        file.write(text)
        file.close()
    
    def file_save_as(self):#not yet
        
        name,type=QtWidgets.QFileDialog.getSaveFileName(self,'Save File',os.getcwd(),'All Files (*);;jpg Files (*.jpg);;png Files (*.png)')
        #img=ImageQt.fromqpixmap(self.label.pixmap())#**
        img=ImageQt.fromqpixmap(self.lb.pixmap())#**
        img.save(name)

         

       
    def color_picker(self):
        
        color=QtWidgets.QColorDialog.getColor()
        self.styleChoice.setStyleSheet('QWidget { background-color: %s}'%color.name())
                                         #不適QtWidgets#
    
    def editor(self):
        self.textEdit=QtWidgets.QTextEdit()
        self.setCentralWidget(self.textEdit)
    
    def font_Choice(self):
        font,valid=QtWidgets.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)
        
        
        
    def style_choice(self,text):
        #self.styleChoice.setText(text)    
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create(text))
    
    def download(self):
        self.completed=0
        while self.completed<100:
            self.completed+=0.0001
            self.progress.setValue(self.completed)
        
    def enlarge_window(self,state):
        if state==QtCore.Qt.Checked:
            self.setGeometry(50,50,1000,600)
        else:
            self.setGeometry(50,50,500,300)
    
    def close_application(self):
        #print('Whona thsi is so cute!!')
        choice=QtWidgets.QMessageBox.question(self,'Information','Confirm information',
                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice==QtWidgets.QMessageBox.Yes:
            print('It is done!')
            print('Whona thsi is so cute!!')
            sys.exit()# close
        else:
            pass
        # self.setWindowTitle('Pyqt5 Tuts!nkkjnj')
    def close_main_application(self):
       
        sys.exit()# close
          
        
if __name__ == "__main__":        
#def run():        
    app=QtWidgets.QApplication(sys.argv)
    GUI=Window()
    sys.exit(app.exec_())
    print(GUI.mro())
    print(MyLabel.mro())
#run()
  
  