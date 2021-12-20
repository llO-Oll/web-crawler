    # for i in range(len(urls)):
    #     try: 
    #         res = urllib.request.urlopen(urls[i])  
    #         html = res.read().decode('utf-8') 
    #         soup = BeautifulSoup(html, 'lxml')            
    #         t=''
    #         temp=''
    #         fatherurl =re.match('https://www.ndrc.gov.cn/xxgk/zcfb/(.*)/',urls[i] )     #匹配根网址，附件url=根+子级url
    #         # if 'tz' in fatherurl.group():
    #         t = soup.find('div',class_="article_con article_con_notitle").get_text()       
    
    #         t=t.replace("　",'\n')                      #解码后的空字符，不是空格，段落标志
    #         t=t.replace("    ",'\n')                    #解码后的空字符，不是空格，段落标志
    #         txt(Titles[i],times[i],t)

    #         #是否存在pdf附件,存在获取url并下载
    #         for a in soup.find_all(href=re.compile(".pdf")):
    #             temp_url=a.get('href')                  # 获取子级url
    #             temp_url=temp_url.replace('./','')      # 替换子级url前面的'./'
    #             print(temp_url)
    #             filename=a.get_text()+'.pdf'
    #             url=fatherurl.group()+temp_url          # 完整的附件url
    #             print(url)
    #             getFile(url,filename)
    #             # print('sucess download'+filename)

    #     except OSError:
    #         pass    #如果报错就不管，继续读取下一个url
    #     continue