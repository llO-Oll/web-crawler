import urllib.request
import urllib.parse

def create_request(page):
    # 定义url
    base_url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=recommend&"
    data = {
        'page_start':(page-1)*20,
        'page_limit':20
    }
    data = urllib.parse.urlencode(data)

    url = base_url + data
    print(url)
    # 请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    request = urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(page,content):
    with open('doban_' + str(page) + '.json','w',encoding='utf-8') as fp:
        fp.write(content)

if __name__ == "__main__":
    start_page = 1
    end_page = 10

    for page in range(start_page,end_page+1):
        request = create_request(page)
        content = get_content(request)
        down_load(page,content)