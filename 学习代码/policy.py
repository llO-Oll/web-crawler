import urllib.request
import requests
import time
import json
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup  
from lxml import etree                  
import os                      

import re

def get(url,headers):   
    count = 0
    titles=[]
    suburls=[]
    times=[]
    res = urllib.request.urlopen(url)  
    html = res.read().decode('utf-8') 
    soup = BeautifulSoup(html, 'lxml')  

    #定位一级网址的政策部分
    a=soup.find('div',class_='content')
    b=a.find_all('li')
    #获取二级网址的政策标题和url
    for t in b:
        titles.append( t.find('a').get_text())
        times.append(t.find('span',class_='data').get_text())
        suburls.append(t.find('a').get('href'))


    for i in range(len(suburls)):
        try: 
            res = urllib.request.urlopen(suburls[i])  
            html = res.read().decode('utf-8') 
            selector = etree.HTML(html)  
            links = selector.xpath('//div[@class="article-content"]/table[4]//text()')
            print(links)
            # for t in links:

            #     txt(titles[i],times[i],t)
            

        except OSError:
            pass    #如果报错就不管，继续读取下一个url
        continue

num=0
filepath='F:/nengyuanju/'     # 政策保存路径
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

    file.write(text)                            #保存正文
    # print(text)
    file.close

if __name__ == '__main__':
    # for i in range(25):
    url='http://www.nea.gov.cn/policy/tz.htm'
    headers={'User-Agent':'Mozilla/5.0(Windows;U;Windows NT6.1;en-US;rv:1.9.1.6) Geko/20091201 Firefox/3.5.6'}#浏览器代理
    get(url,headers)