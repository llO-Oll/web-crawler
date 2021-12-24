# - * - coding:utf-8 - *
from time import sleep
from model.model import BaiduModel
import os
import time
import json
text=''
filepath='F:/国家发改委四类政策/能源局政策_摘要/'
path = 'F:/国家发改委四类政策/能源局政策/'

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
    print(text)
    file.close




for file in os.listdir(path):
    try:
        if not os.path.isdir(file):
            print(file)
            name=''
            data=''
            text=[]
            temp=''
            result=''
            f=open(path+file,'r', encoding='utf-8')
            for num, line in enumerate(f):
                if num==0:
                    name=line
                if num==1:
                    data=line
                if num > 3:
                    line=line.replace(" ",'')
                    line=line.replace(" ",'')
                    line=line.replace(" ",'')
                    line=line.replace("    ",'')                   #解码后的空字符，不是空格，段落标志    
                    text.append(line)
            
            result_nlp=model.getSummary(''.join(text))
            print(result_nlp)
            if result_nlp.get('summary')!=None:
                time.sleep(0.5)
                txt(file,name,data, result_nlp.get('summary'))

            elif result_nlp.get('error_msg')=='input text too long':
                for i in text:
                    temp=model.getSummary(i).get('summary')
                    time.sleep(0.5)
                    if temp!=None:  
                        result=result+temp
                txt(file,name,data, result) 
    except json.decoder.JSONDecodeError:
        pass   