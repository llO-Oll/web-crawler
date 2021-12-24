# - * - coding:utf-8 - *
from time import sleep
from model.model import BaiduModel
import os
import time
import json
filepath='F:/国家发改委四类政策/国家发改委电力政策_摘要/'
file1 = '229.txt'
path = 'F:/国家发改委四类政策/国家发改委电力政策/'
model = BaiduModel()
def txt(filename,name,time, text):  

    global num
    if not os.path.exists(filepath):  # 路径不存在时创建一个
        os.makedirs(filepath)

    savepath = filepath+filename
    num=num+1
    file = open(savepath, 'a', encoding='utf-8')    #因为一个网页里有多个标签p或者span，所以用'a'添加模式
    
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
        line=line.replace(" ",'')
        line=line.replace(" ",'')
        line=line.replace(" ",'')
        
        # line=line.replace("　",'\n')                      #解码后的空字符，不是空格，段落标志
        # line=line.replace("   ",'\n')                    #解码后的空字符，不是空格，段落标志
        line=line.replace(" ",'\n')
        text.append(line)
text1=''.join(text)
print(text1)
txt(file1,name,data, text1) 

result_nlp=model.getSummary(''.join(text))
print(result_nlp)
if result_nlp.get('summary')!=None:
    time.sleep(0.5)
    txt(file1,name,data, result_nlp.get('summary'))

elif result_nlp.get('error_msg')=='input text too long':
    for i in text:
        temp=model.getSummary(i).get('summary')
        time.sleep(0.5)
        if temp!=None:  
            result=result+temp
    txt(file1,name,data, result) 
