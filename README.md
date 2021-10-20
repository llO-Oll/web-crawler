# 网络爬虫

当我们在浏览器中输入一个url后回车，后台会发生什么？比如说你输入http://www.lining0806.com/，你就会看到宁哥的小站首页。

简单来说这段过程发生了以下四个步骤：

- 查找域名对应的IP地址。
- 向IP对应的服务器发送请求。
- 服务器响应请求，发回网页内容。
- 浏览器解析网页内容。

**网络爬虫要做的，简单来说，就是实现浏览器的功能。通过指定url，直接返回给用户所需要的数据，而不需要一步步人工去操纵浏览器获取。**

***

## 相关知识

***URL***

我们在浏览器的地址栏里输入的网站地址叫做URL (Uniform Resource Locator，统一资源定位符)。就像每家每户都有一个门牌地址一样，每个网页也都有一个Internet地址。当你在浏览器的地址框中输入一个URL或是单击一个超级链接时，URL就确定了要浏览的地址。浏览器通过超文本传输协议(HTTP)，将Web服务器上站点的网页代码提取出来，并翻译成漂亮的网页。因此，在我们认识HTTP之前，有必要先弄清楚URL的组成,例如：http://www.baidu.com/china/index.htm。它的含义如下：

1. **http://**：代表超文本传输协议，通知baidu.com服务器显示Web页，通常不用输入；

2. **www**：代表一个Web（万维网）服务器；

3. **baidu.com/**：这是装有网页的服务器的域名，或站点服务器的名称；

4. **China/**：为该服务器上的子目录，就好像我们的文件夹；

5. **Index.htm**：index.htm是文件夹中的一个H搜索TML文件（网页）



URL一般格式

```
protocol :// hostname[:port] / path / [;parameters][?query]#fragment
```

1. protocol(协议)：
   指定使用的传输协议，下面也列出了几种protocol属性的有效方案名称。那我们最常用的就是HTTP协议，它也是目前www中应用最广泛的协议。
   file 资源是本地计算机上的文件。格式file:///，注意后边应是三个斜杠。
   ftp 通过 FTP访问资源。格式 FTP://
   gopher 通过 Gopher 协议访问该资源。
   http 通过 HTTP 访问该资源。 格式 HTTP://
   https 通过安全的 HTTPS 访问该资源。 格式 HTTPS://
   mailto 资源为电子邮件地址，通过 SMTP 访问。 格式 mailto:

2. hostname(主机名)

   是指存放资源的服务器的域名系统(DNS) 主机名或 IP 地址。有时，在主机名前也可以包含连接到服务器所需的用户名和密码（格式：username:password@hostname）。

3. port(端口号)

   整数，可选，省略时使用方案的默认端口，各种传输协议都有默认的端口号，如http的默认端口为80。如果输入时省略，则使用默认端口号。有时候出于安全或其他考虑，可以在服务器上对端口进行重定义，即采用非标准端口号，此时，URL中就不能省略端口号这一项。

4. path（路径）

   由零或多个“/”符号隔开的字符串，一般用来表示主机上的一个目录或文件地址。

5. parameters（参数）
   这是用于指定特殊参数的可选项。

6. query(查询)

   可选，用于给动态网页（如使用CGI、ISAPI、PHP/JSP/ASP/ASP。NET等技术制作的网页）传递参数，可有多个参数，用“&”符号隔开，每个参数的名和值用“=”符号隔开。

7. fragment（信息片断）

   字符串，用于指定网络资源中的片断。例如一个网页中有多个名词解释，可使用fragment直接定位到某一名词解释。

[URL格式_hhthwx的博客-CSDN博客_url](https://blog.csdn.net/hhthwx/article/details/78567961)



***get&post***

- **GET** - 从指定的资源请求数据。
- **POST** - 向指定的资源提交要被处理的数据。

[GET 和 POST 到底有什么区别？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/28586791)

***

## Scrapy

