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
# 页面url地址
s="../../1310346788_16384121000351n.docx"
s=s.replace('../','')
print(s)
# url='http://zfxxgk.nea.gov.cn/2021-11/08/c_1310304917.htm'
# headers={'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) '}#浏览器代理
# res=requests.get(url,headers=headers)
# # res = urllib.request.urlopen(url)  
# # html = res.read().decode('utf-8') 
# selector = etree.HTML(res.text)  
# links = selector.xpath('//div[@class="article-content"]/table[4]//text()')
