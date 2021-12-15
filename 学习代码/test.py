import urllib.request
import requests
import time
import json
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup  # 导入urllib库的request模块
import lxml                    #文档解析器
import os                      #os模块就是对操作系统进行操作
from lxml import etree   
import re

url='https://www.ndrc.gov.cn/xxgk/zcfb/tz/202112/t20211208_1307104.html?code=&state=123'
headers={'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) '}#浏览器代理
res = urllib.request.urlopen(url)  
html = res.read().decode('utf-8') 
soup = BeautifulSoup(html, 'lxml')            

num=0
filepath='F:/test/'     # 政策保存路径
def txt(name,time, text):  
    global num
    if not os.path.exists(filepath):  # 路径不存在时创建一个
        os.makedirs(filepath)
    savepath = filepath+str(num)+ '.txt'
    num=num+1
    file = open(savepath, 'a', encoding='utf-8')    #因为一个网页里有多个标签p或者span，所以用'a'添加模式
    
    file.write(name)
    file.write('\r')
    file.write(time)
    file.write('\r')
    file.write('国家发改委')
    file.write('\r')
    # text=text.replace('<em>','')
    # text=text.replace('</em>','')               #剔除由关键字搜索产生的'<em>关键词</em>'
    print(text)
    file.write(text)                            #保存正文
    # print(text)
    file.close

t=''
temp=''
span_lables = soup.select('span')
for span in span_lables:
    if span.get_text()!=temp:
        temp = span.get_text()

        print(temp) 
        t =t+'\r'+temp
    
txt('test','test',t)
