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

url='http://zfxxgk.nea.gov.cn/2021-11/08/c_1310304917.htm'
res = urllib.request.urlopen(url)  
html = res.read().decode('utf-8') 
selector = etree.HTML(html)  
links = selector.xpath('//div[@class="article-content"]/table[4]//text()')
print(links)

