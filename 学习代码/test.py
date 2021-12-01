import urllib.request
import requests
import time
import json
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup  # 导入urllib库的request模块
import lxml                    #文档解析器
import os                      #os模块就是对操作系统进行操作
import re
# 页面url地址


url = 'https://www.ndrc.gov.cn/xxgk/zcfb/fzggwl/202009/t20200923_1239477.html'
fatherurl =re.match('https://www.ndrc.gov.cn/xxgk/zcfb/(.*)/',url)
res = urllib.request.urlopen(url)  
html = res.read().decode('utf-8') 
soup = BeautifulSoup(html, 'lxml')    
t=''


picpath='F:/test/'
def txt(name,time, text):  # 定义函数名
    if not os.path.exists(picpath):  # 路径不存在时创建一个
        os.makedirs(picpath)
    savepath = picpath+ 'test.txt'
    file = open(savepath, 'a', encoding='utf-8')#因为一个网页里有多个标签p，所以用'a'添加模式
    file.write(name)
    file.write('\r')
    file.write(time)
    file.write('\r')
    file.write('国家发改委')
    file.write('\r')
    # text=text.replace('  ','\r')
    file.write(text)
    # print(text)
    file.close
txt('TEST','2021',t)

def getFile(url,file_name):
    try:
        u = urllib.request.urlopen(url)
    except urllib.error.HTTPError:
       #碰到了匹配但不存在的文件时，提示并返回
        print(url, "url file not found")
        return
    if not os.path.exists(picpath):  # 路径不存在时创建一个
        os.makedirs(picpath)
    block_sz = 8192
    with open(picpath+file_name+'.pdf', 'wb') as f:
        while True:
            buffer = u.read(block_sz)
            if buffer:
                f.write(buffer)
            else:
                break
for p in soup.select('span'):
    temp = p.get_text()
    t =t+'\r'+temp
for a in soup.find_all(href=re.compile(".pdf")):
    temp_url=a.get('href')
    temp_url=temp_url.replace('./','')
    print(temp_url)
    filename=a.get_text()
    url=fatherurl.group()+temp_url
    print(url)
    getFile(url,filename)

