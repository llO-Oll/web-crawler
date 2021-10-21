import urllib3 

# 使用urllib3.disable_warnings()在关闭SSL认证（verify=False）情况下

# 将requests请求禁用安全请求警告

import requests    # 使用Requests发送网络请求

import time      # 用来获取时间戳(计算当前时间，用于网页验证)

import json      # 处理json文件

import numpy as np  # 处理数组

import pandas as pd  # np.array()转换成pd.DataFrame格式，再使用to_excel()写入excel表格



# 获取毫秒级时间戳，用于网页验证

def getTime():

  return int(round(time.time() * 1000))



# 数据预处理，获取json列表中层层包裹的strdata元素（数据）

def getList(length):

  List=[]

  for i in range(length):

    temp = js['returndata']['datanodes'][i]['data']['strdata']

    # 城乡居民收支列表中，原网站有同比增长数据为空，若直接使用eval()会报错，需要先判断

    if(len(temp)!=0):

    # eval()数字转字符串

        List.append(eval(temp))

  return List

if __name__ == '__main__':

  # 请求目标网址(链接?前面的东西)

  url='https://data.stats.gov.cn/easyquery.htm'

  # 请求头，User-Agent: 用来证明你是浏览器，满足一定格式即可，不一定和自己的浏览器一样

  headers={'User-Agent':'Mozilla/5.0(Windows;U;Windows NT6.1;en-US;rv:1.9.1.6) Geko/20091201 Firefox/3.5.6'}#浏览器代理



  # 构造参数键值对，具体数值从网页结构参数中获取

  key={}

  key['m']='QueryData'

  key['dbcode']='fsnd'

  key['rowcode']='reg'

  key['colcode']='sj'

  key['wds']='[{"wdcode":"zb","valuecode":"A020101"}]'

  key['k1']=str(getTime()) 

  # "wdcode":"reg" 地区栏

  # 上海 310000 

  key['dfwds']='[{"wdcode":"sj","valuecode":"LAST10"}]'

  # "wdcode":"zb" 选取左侧哪个条目,"wdcode":"sj"选项框中选取"最近6季度"

  # 禁用安全请求警告

  requests.packages.urllib3.disable_warnings()

  # 发出请求，使用post方法，这里使用前面自定义的头部和参数

  # ！！！verify=False，国家统计局20年下半年改用https协议,若不加该代码无法通过SSL验证

  r = requests.post(url, headers=headers, params=key,verify=False)

  # 使用json库中loads函数，将r.text字符串解析成dict字典格式存储于js中

  js = json.loads(r.text)



  # 得到所需数据的一维数组，利用np.array().reshape()整理为二维数组

  length=len(js['returndata']['datanodes'])

  res=getList(length)

  # 总数据划分成6行的格式

  array=np.array(res).reshape(len(res)//10,10)



  # np.array()转换成pd.DataFrame格式，后续可使用to_excel()直接写入excel表格

  df_shanghai=pd.DataFrame(array)
  list_2 = js['returndata']['wdnodes'][2]['nodes']
  index_list = []
  for i_2 in range(len(list_2)):
    index = list_2[i_2]['cname']
    index_list.append(index)
    print(index_list)
  print('*'*20+'\n')
# 获取列名称
  list_3 = js['returndata']['wdnodes'][1]['nodes']
  columns_list = []
  for i_2 in range(len(list_3)):
    columns = list_3[i_2]['cname']
    columns_list.append(columns)
  df_shanghai.columns=index_list

  df_shanghai.index=columns_list



  print(df_shanghai)
  write = pd.ExcelWriter('./地区生产总值.xls') #该路径自己设置即可，没有该文件的话会自行创建一个，存在的话写入会覆盖原内容
  df_shanghai.to_excel(write)
    #如果爬多个省份的数据，可以写入多个工作表，且必须要加上save()保存
  write.save()