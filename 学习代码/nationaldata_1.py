import urllib.request
import requests
import time
import json
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup  # 导入urllib库的request模块
import lxml                    #文档解析器
import os                      #os模块就是对操作系统进行操作




def get(url):


    # 禁用安全请求警告
    requests.packages.urllib3.disable_warnings()

    # 发出请求，使用post方法，这里使用前面自定义的头部和参数
    # verify=False，国家统计局20年下半年改用https协议,若不加该代码无法通过SSL验证
    r = requests.post(url, headers=headers,verify=False)

    # 使用json库中loads函数，将r.text字符串解析成dict字典格式存储于js中
    js = json.loads(r.text)
    # print(js)

# 数据预处理，获取json列表中层层包裹的strdata元素（数据）
    def getList(length):
        Titles=[]
        urls=[]
        for i in range(length):
            Title = js['data']['resultList'][i]['dreTitle']
            time = js['data']['resultList'][i]['docDate']
            organization = js['data']['resultList'][i]['domainSiteName']
            suburl = js['data']['resultList'][i]['url']
            print(Title+time+organization+suburl)

            Titles.append(Title)
            urls.append(suburl)

        return Titles,urls


    length=len(js['data']['resultList'])
    Titles,urls=getList(length)




    for i in range(len(urls)):
        try: 
            res = urllib.request.urlopen(urls[i])  
            html = res.read().decode('utf-8') 
            soup = BeautifulSoup(html, 'lxml')

            print(str(i)+'saved')
            for p in soup.select('p'):
                t = p.get_text()
                t.replace(' ','\r\n')
                txt(Titles[i],t)
            for span in soup.select('span'):
                t = span.get_text()
                t.replace(' ','\r\n')
                txt(Titles[i],t)                
        except OSError:
            pass    #如果报错就不管，继续读取下一个url
        continue
    
#定义txt存储路径。
picpath='./newws/'#这里我用的是本程序路径，也可改为c盘或d盘等路径。
def txt(name, text):  # 定义函数名
    if not os.path.exists(picpath):  # 路径不存在时创建一个
        os.makedirs(picpath)
    savepath = picpath + name + '.txt'
    file = open(savepath, 'a', encoding='utf-8')#因为一个网页里有多个标签p，所以用'a'添加模式

    file.write(text)
    file.write('\r')
    # print(text)
    file.close
if __name__ == '__main__':
    for i in range(5):
        url='https://fwfx.ndrc.gov.cn/api/query?qt=&tab=all&page='+str(i)+'&pageSize=20&siteCode=bm04000fgk&key=CAB549A94CF659904A7D6B0E8FC8A7E9&startDateStr=&endDateStr=&timeOption=0&sort=dateDesc'
        headers={'User-Agent':'Mozilla/5.0(Windows;U;Windows NT6.1;en-US;rv:1.9.1.6) Geko/20091201 Firefox/3.5.6'}#浏览器代理
        get(url)

