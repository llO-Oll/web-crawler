# - * - coding:utf-8 - *
from time import sleep
from model.model import BaiduModel
import os
import time
import json
filepath='F:/国家发改委四类政策/国家发改委电力政策_摘要/'
file1 = '395.txt'
path = 'F:/国家发改委四类政策/国家发改委电力政策/'
model = BaiduModel()
def txt(filename,name,time, text):  

    global num
    if not os.path.exists(filepath):  # 路径不存在时创建一个
        os.makedirs(filepath)

    savepath = filepath+filename
    num=num+1
    file = open(savepath, 'w', encoding='utf-8')    #因为一个网页里有多个标签p或者span，所以用'a'添加模式
    
    file.write(name)
    file.write(time)
    file.write('国家发改委')
    file.write('\r')
    file.write(text)                            #保存摘要
    file.close






print(file1)
name=''
data=''
text=[]
temp=''
result=''
f=open(path+file1,'r', encoding='utf-8')
for num, line in enumerate(f):
    if num==0:
        name=line
    if num==1:
        data=line
    if num > 3:        
        line=line.replace("　　",'\n')
        line=line.replace("   ",'\n')
        line=line.replace(" ",'\n')
        
        text.append(line)
text1=''.join(text)
print(text1)
f.close
# txt(file1,name,data, text1)
