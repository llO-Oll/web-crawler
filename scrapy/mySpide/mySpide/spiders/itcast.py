import scrapy
from scrapy import item
from mySpide.items import Itcastltem

# class ItcastSpider(scrapy.Spider):
#     name = 'itcast'
#     allowed_domains = ['itcast.cn']
#     start_urls = ['http://itcast.cn/channel/teacher.shtml']

# class Opp2Spider(scrapy.Spider):
    
#     name = 'itcast'                 #name ：标识蜘蛛。它在一个项目中必须是唯一的，即不能为不同的爬行器设置相同的名称。
#     allowed_domains = ['itcast.com']
#     start_urls = ['http://www.itcast.cn/']


#     def parse(self, response):
#         #获取网站标题
#         context = response.xpath('/html/head/title/text()')

#         #提取网站标题
#         title = context.extract_first()  
#         print(title) 
        
#         pass        

def parse(self, response):
    
    # 存放老师信息的集合
    items = []

    for each in response.xpath("//div[@class='li_txt']"):
        #将我们得到的数据封装到一个‘ItcastItem’对象
        item = Itcastltem()

        #extract()方法返回的都是unicode字符串
        name = each.xpath("h3/text()").extract()
        print(name)
        title = each.xpath("h4/text()").extract()
        info = each.xpath("p/text()").extract()
        items.append(item)

    return items