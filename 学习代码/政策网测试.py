import requests
import json
from bs4 import BeautifulSoup
import re
import os
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 FS"}

def get_html(url):
    r = requests.get(url=url, headers=headers)
    r.encoding = r.apparent_encoding
    print("状态：", r.raise_for_status)
    return r.text

def get_json(url):
    r = requests.get(url=url, headers=headers)
    r.encoding = r.apparent_encoding
    print("状态：", r.raise_for_status)
    return r.json()

def get_url_list(json_text):
    url_dict = dict()
    for each in json_text['searchVO']['catMap']['gongwen']['listVO']:
        url_dict[each['url']] = each['title'].replace('<em>','').replace('</em>','')
    for each in json_text['searchVO']['catMap']['otherfile']['listVO']:
        url_dict[each['url']] = each['title'].replace('<em>','').replace('</em>','')
    return url_dict

def get_all_link():
    url_dict = dict()
    for i in range(0,30):
        print(i)
        url=f'http://sousuo.gov.cn/data?t=zhengcelibrary&q=%E7%94%B5%E5%8A%9B&timetype=&mintime=&maxtime=&sort=&sortType=1&searchfield=&pcodeJiguan=&childtype=&subchildtype=&tsbq=&pubtimeyear=&puborg=&pcodeYear=&pcodeNum=&filetype=&p={i}&n=5&inpro=&bmfl=&dup=&orpro='
        json_text = get_json(url)
        dic = get_url_list(json_text)
        print(dic)
        if not dic:
            break
        url_dict.update(dic)
    return url_dict

def save_file(url, title):
    text = get_html(url)
    soup = BeautifulSoup(text, 'lxml')
    fp = open(f'F:/file/{title}.txt', 'a', encoding='utf-8')
    for each in soup.find_all('p'):
        if each.string:
            fp.writelines(each.string)
    fp.close()
    print("写入成功")

def main():
    if not os.path.exists('F:/file/'):
        os.makedirs('F:/file/')
    url_dict = get_all_link()
    for url in url_dict:
        save_file(url, url_dict[url])

main()
