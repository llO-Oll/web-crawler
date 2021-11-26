
import urllib.request
import requests
import time
import json
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup  # 导入urllib库的request模块
import lxml                    #文档解析器
import os                      #os模块就是对操作系统进行操作

count = 0
def get(url,headers):

    # 禁用安全请求警告
    requests.packages.urllib3.disable_warnings()

    # 发出请求，使用post方法，这里使用前面自定义的头部和参数
    # verify=False，国家统计局20年下半年改用https协议,若不加该代码无法通过SSL验证
    r = requests.post(url, headers=headers,verify=False)

    # 使用json库中loads函数，将r.text字符串解析成dict字典格式存储于js中
    js = json.loads(r.text)

    length=len(js['data']['resultList'])
    return js,length

# 分析json
def getList(js,length):
    Titles=[]
    urls=[]
    times=[]
    global count
    for i in range(length):
        Title = js['data']['resultList'][i]['dreTitle']
        time = js['data']['resultList'][i]['docDate']
        organization = js['data']['resultList'][i]['domainSiteName']
        suburl = js['data']['resultList'][i]['url']
        count=count+1
        print(str(count)+Title+time+organization+suburl)
        if 'pdf' not in suburl:
            Title.replace("<em>","")
            Title.replace("</em>","")
            print(Title)
            Titles.append(Title)
            urls.append(suburl)
            times.append(time)
    # return Titles,urls,times

    for i in range(len(urls)):
        try: 
            res = urllib.request.urlopen(urls[i])  
            html = res.read().decode('utf-8') 
            soup = BeautifulSoup(html, 'lxml')

            
            t=''
            for p in soup.select('p'):
                temp = p.get_text()
                t =t+temp
            txt(Titles[i],times[i],t)
        except OSError:
            pass    #如果报错就不管，继续读取下一个url
        continue
num=0
picpath='F:/xlx/'
def txt(name,time, text):  # 定义函数名
    global num
    if not os.path.exists(picpath):  # 路径不存在时创建一个
        os.makedirs(picpath)
    savepath = picpath+str(num)+ '.txt'
    num=num+1
    file = open(savepath, 'a', encoding='utf-8')#因为一个网页里有多个标签p，所以用'a'添加模式
    file.write(name)
    file.write('\r')
    file.write(time)
    file.write('\r')
    file.write('国家发改委')
    file.write('\r')
    file.write(text)
    # print(text)
    file.close

if __name__ == '__main__':
    for i in range(20):
        url='https://fwfx.ndrc.gov.cn/api/query?qt=%E7%94%B5%E5%8A%9B&tab=all&page='+str(num)+'&pageSize=20&siteCode=bm04000fgk&key=CAB549A94CF659904A7D6B0E8FC8A7E9&startDateStr=&endDateStr=&timeOption=0&sort=weight'
        headers={'User-Agent':'Mozilla/5.0(Windows;U;Windows NT6.1;en-US;rv:1.9.1.6) Geko/20091201 Firefox/3.5.6'}#浏览器代理
        js,length=get(url,headers)
        getList(js,length)