import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import time
import json

def getTime():
    return int(round(time.time() * 1000))


url='http://data.stats.gov.cn/easyquery.htm?cn=A01'
headers={'User-Agent':'Mozilla/5.0(Windows;U;Windows NT6.1;en-US;rv:1.9.1.6) Geko/20091201 Firefox/3.5.6'}#浏览器代理
key={}#参数键值对
key['m']='QueryData'
key['dbcode']='fsnd'
key['rowcode']='reg'
key['colcode']='sj'
key['wds']='[{"wdcode":"zb","valuecode":"A020101"}]'
key['dfwds']='[]'
key['k1']=str(getTime())
r=requests.get(url,headers=headers,params=key)
js=json.loads(r.text)
js

list_2 = js['returndata']['wdnodes'][2]['nodes']
index_list = []
for i_2 in range(len(list_2)):
    index = list_2[i_2]['cname']
    index_list.append(index)
    print(index)
 
# 获取列名称
list_3 = js['returndata']['wdnodes'][1]['nodes']
columns_list = []
for i_2 in range(len(list_2)):
    columns = list_2[i_2]['cname']
    columns_list.append(columns)
    print(columns)