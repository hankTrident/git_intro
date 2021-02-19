# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 23:31:32 2020

@author: Wish
"""
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from pyquery import PyQuery as pq
import time

from moviepy.editor import VideoFileClip as vclp
from moviepy.editor import concatenate_videoclips as concat
import os
import moviepy.editor as mpe
import re
import imageio
   
url='http://ocw.nthu.edu.tw/ocw/index.php?page=chapter&cid=256&chid=2873'
urls=[]
html=pq(url)
chop = webdriver.ChromeOptions()
#chop.add_extension('C:/Users/Wish/.spyder-py3/CRX/extension_0_1_0_0.crx')
#chop.add_extension('C:/Users/Wish/.spyder-py3/CRX/adblock.crx')
#chop.add_argument('headless')
chop.add_extension('C:/Users/HankWu/Documents/Python Scripts/CRX/extension_0_1_0_0.crx')
chop.add_extension('C:/Users/HankWu/Documents/Python Scripts/CRX/adblock.crx')
driver = webdriver.Chrome(chrome_options = chop)
#driver = webdriver.Chrome('C:/Users/HankWu/chromedriver/chromedriver.exe',chrome_options = chop)
driver.get(url)
#time.sleep(5)
b=driver.find_elements(By.CSS_SELECTOR,'a[href$="{}"]'.format(url.split('chapter&')[-1]))
for i in range(len(b)):
     b[i].send_keys(Keys.RETURN)
hand=driver.window_handles     
for i in range(len(hand)):
    driver.switch_to_window(hand[i])
    urls.append(driver.current_url)
urls=sorted(urls)
for i in range(2,len(urls)):
    print(urls[i])
#=== 先改黨名為1   ====
def mp4_render(a):
    for i in range(1,4):
          clip=vclp('E:/Downloads1/cloudCC/1 ({}).mp4'.format(i))
          clip.write_videofile('E:/Downloads1/cloudCC/lec{}-{}.mp4'.format(a,i),codec='libx264')
#          clip=vclp('C:/Users/HankWu/Downloads/cloudCC/1 ({}).mp4'.format(i))          ###合併clip1 clip2轉檔
#          clip.write_videofile('C:/Users/HankWu/Downloads/cloudCC/lec4-{}.mp4'.format(i),codec='libx264')    
if __name__ =="mp4_render":                                   #要改
    mp4_render() 
    
    