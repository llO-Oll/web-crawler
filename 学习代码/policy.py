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
            soup = BeautifulSoup(html, 'lxml')
            selector = etree.HTML(html)  
            links = selector.xpath('//div[@class="article-content"]/table[4]//text()'.strip())
            t = ''.join(links)
            if t!='' and '电' in titles[i]:
                fatherurl =re.match('http://zfxxgk.nea.gov.cn/(.*)/',suburls[i]).group()     #匹配根网址，附件url=根+子级url 
                txt(titles[i],times[i],t)
                            #是否存在pdf附件,存在获取url并下载
                for a in soup.find_all(href=re.compile(".doc|.docx")):
                    temp_url=a.get('href')              # 获取子级url
       
                    print(temp_url)
                    if '../'  in temp_url:
                        temp_url=temp_url.replace('../','')
                        fatherurl='http://zfxxgk.nea.gov.cn/'
                        url=fatherurl+temp_url          # 完整的附件url
                    elif 'http' in temp_url:
                        url=temp_url 
                    else:
                        temp_url=temp_url.replace('./','')
                        url=fatherurl+temp_url          # 完整的附件url
                    filename=a.get_text().strip()+'.doc'
                    print(url)
                    getFile(url,filename)
                    print('sucess download'+filename)

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
    file.write('国家能源局')

    file.write(text)                            #保存正文
    print(num)
    file.close

#下载附件
def getFile(url,file_name):
    try:
        u = urllib.request.urlopen(url)
    except urllib.error.HTTPError:
       #碰到了匹配但不存在的文件时，提示并返回
        print(url, "url file not found")
        return
    if not os.path.exists(filepath):  # 路径不存在时创建一个
        os.makedirs(filepath)
    block_sz = 8192
    with open(filepath+file_name, 'wb') as f:
        while True:
            buffer = u.read(block_sz)
            if buffer:
                f.write(buffer)
            else:
                break

if __name__ == '__main__':
    url='http://www.nea.gov.cn/policy/tz.htm'
    headers={'User-Agent':'Mozilla/5.0(Windows;U;Windows NT6.1;en-US;rv:1.9.1.6) Geko/20091201 Firefox/3.5.6'}#浏览器代理
    get(url,headers)
    for i in range(2,18):
        url='http://www.nea.gov.cn/policy/tz_'+str(i)+'.htm'
        get(url,headers)