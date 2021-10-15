from urllib import request

import re

def getReq(url):

    url_req = request.urlopen(url)

    return url_req

web_and_page = []

http_req = getReq("http://www.hb.sgcc.com.cn/html/main/col64/column_64_1.html")

data = http_req.read().decode('utf-8')

# tr = re.findall(r'<li> <a target="_blank" href=(.*)>(.*)</a> <span>',data)
tr = re.findall(r'<li> <a target="_blank" href=(.*)>(.*)</a> <span>',data)
firsttable = tr[0][0]
print(len(tr))
# for i in len(tr):
#     tr[i][0]=""
str=str(tr)
print(str)
outfile = open('湖北省电网政策.txt','w')
outfile.write(str)
outfile.close()
# def getHtml(data):

#     htmllist = re.findall(r'href="(.*?)</a></li>',firsttable)

#     return htmllist

# htmllist = getHtml(data)

# outfile = open('爬取网络小说神印王座的章节目录的网址1.txt','w')

# for hl in htmllist:

#     newurl = "https://www.9dxs.com/1/1026/"+hl

#     firsttable = newurl.replace('">', ' ')

#     print(firsttable)

# outfile.write(firsttable+'\n')

# outfile.close()
