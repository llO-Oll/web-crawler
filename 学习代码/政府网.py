import urllib.request
import requests
import time
import json
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup  
import lxml                    
import os                      
from tqdm import tqdm
import re
import random
from model.model import BaiduModel
count = 0


def get(url,headers):   
    requests.packages.urllib3.disable_warnings()    # 禁用安全请求警告

    # 发出请求，使用post方法，这里使用前面自定义的头部和参数
    # verify=False,https协议,若不加该代码无法通过SSL验证
    r = requests.post(url,headers=headers)
    print(r.text)
    js = json.loads(r.text)    # 使用json库中loads函数，将r.text字符串解析成dict字典格式存储于js中

    return js

# 分析json
def getList(js):
    Titles=[]
    urls=[]
    times=[]
    fujianurl=[]
    global count
    length_bumen=len(js['searchVO']['catMap']['bumenfile']['listVO'])
    length_gongwen=len(js['searchVO']['catMap']['gongwen']['listVO'])
    #lenth_otherfile=len(js['searchVO']['catMap']['otherfile']['listVO'])
    
    #从一级网址获取信息
    for i in range(length_bumen):
        Title = js['searchVO']['catMap']['bumenfile']['listVO'][i]['title']                #政策标题
        time = js['searchVO']['catMap']['bumenfile']['listVO'][i]['pubtimeStr']                   #政策发布时间
        organization = js['searchVO']['catMap']['bumenfile']['listVO'][i]['puborg']    #机构
        suburl = js['searchVO']['catMap']['bumenfile']['listVO'][i]['url']                  #二级网址    

        count=count+1
        Title=Title.replace('<em>','')
        Title=Title.replace('</em>','')    #剔除由关键字搜索产生的'<em>关键词</em>'   
        Titles.append(Title)
        urls.append(suburl)
        times.append(time)
        print(str(count)+Title+time+organization+suburl)

    for i in range(length_gongwen):
        Title = js['searchVO']['catMap']['gongwen']['listVO'][i]['title']                #政策标题
        time = js['searchVO']['catMap']['gongwen']['listVO'][i]['pubtimeStr']                   #政策发布时间
        organization = js['searchVO']['catMap']['gongwen']['listVO'][i]['puborg']    #机构
        suburl = js['searchVO']['catMap']['gongwen']['listVO'][i]['url']                  #二级网址    

        count=count+1
        Title=Title.replace('<em>','')
        Title=Title.replace('</em>','')    #剔除由关键字搜索产生的'<em>关键词</em>'   
        Titles.append(Title)
        urls.append(suburl)
        times.append(time)
        print(str(count)+Title+time+organization+suburl)    

    #爬取二级url
    # for i in range(len(urls)):
    #     try: 
    #         res = urllib.request.urlopen(urls[i])  
    #         html = res.read().decode('utf-8') 
    #         soup = BeautifulSoup(html, 'lxml')            
    #         t=''
    #         temp=''
    #         fatherurl =re.match('https://www.ndrc.gov.cn/xxgk/zcfb/(.*)/',urls[i] )     #匹配根网址，附件url=根+子级url
    #         # if 'tz' in fatherurl.group():
    #         t = soup.find('div',class_="article_con article_con_notitle").get_text()       
    
    #         t=t.replace("　",'\n')                      #解码后的空字符，不是空格，段落标志
    #         t=t.replace("    ",'\n')                    #解码后的空字符，不是空格，段落标志
    #         txt(Titles[i],times[i],t)

    #         #是否存在pdf附件,存在获取url并下载
    #         for a in soup.find_all(href=re.compile(".pdf")):
    #             temp_url=a.get('href')                  # 获取子级url
    #             temp_url=temp_url.replace('./','')      # 替换子级url前面的'./'
    #             print(temp_url)
    #             filename=a.get_text()+'.pdf'
    #             url=fatherurl.group()+temp_url          # 完整的附件url
    #             print(url)
    #             getFile(url,filename)
    #             # print('sucess download'+filename)

    #     except OSError:
    #         pass    #如果报错就不管，继续读取下一个url
    #     continue

#保存政策txt
num=0
filepath='F:/policies/'     # 政策保存路径
def txt(name,time, text):  
    global num
    if not os.path.exists(filepath):  # 路径不存在时创建一个
        os.makedirs(filepath)
    savepath = filepath+name+' '+time+' 国家发改委'+ '.txt'
    num=num+1
    file = open(savepath, 'a', encoding='utf-8')    #因为一个网页里有多个标签p或者span，所以用'a'添加模式
    
    file.write(name)
    file.write('\r')
    file.write(time)
    file.write('\r')
    file.write('国家发改委')
    file.write('\r')
    text=text.replace('<em>','')
    text=text.replace('</em>','')               #剔除由关键字搜索产生的'<em>关键词</em>'
    file.write(text)                            #保存正文
    # print(text)
    file.close

#下载pdf
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
    print ("Sucessful to download" + " " + file_name)


if __name__ == '__main__':
    for i in range(0,99):
        print(i)
        #关键字：电力
        url='http://sousuo.gov.cn/data?t=zhengcelibrary&q=%E7%94%B5%E5%8A%9B&timetype=&mintime=&maxtime=&sort=&sortType=1&searchfield=&pcodeJiguan=&childtype=&subchildtype=&tsbq=&pubtimeyear=&puborg=&pcodeYear=&pcodeNum=&filetype=&p=1&n=5&inpro=&bmfl=&dup=&orpro='
        head_user_agent = ['Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                       'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
                       'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
                       'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
                       'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11']
        headers={'User-Agent':head_user_agent[random.randrange(0,len(head_user_agent))]}#浏览器代理
        js=get(url,headers)
        getList(js)