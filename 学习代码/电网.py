from urllib import request

import re

def getReq(url):

    url_req = request.urlopen(url)

    return url_req

web_and_page = []

http_req = getReq("http://www.hb.sgcc.com.cn/html/main/col64/column_64_1.html")

data = http_req.read().decode('utf-8')

# tr = re.findall(r'<li> <a target="_blank" href=(.*)>(.*)</a> <span>',data)
tr = re.findall(r'<li> <a target="_blank" href="(.*)</a> <span>',data)
firsttable = tr[0]

for html in tr:
    url="http://www.hb.sgcc.com.cn"+html
    url = url.replace('>', '')
    url = url.replace('\"', ' ')
    outfile = open('湖北省电网政策.txt','a')
    print(url)
    outfile.write(url+'\n')
outfile.close()
