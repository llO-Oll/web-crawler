import os
path = "F:/GJFGW" #文件夹目录
newpath ="F:/xlx"
files= os.listdir(path) #得到文件夹下的所有文件名称
s = []
num =0
for file in files: #遍历文件夹
    if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
        os.rename(path+"/"+file,newpath+"/"+str(num)+'.txt')
        num+=1
        print(num) #打印结果