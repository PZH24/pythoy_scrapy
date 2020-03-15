# import os
# os.system('scrapy crawl doubanSpider')
# 测试解析器。
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
html = """<!DOCTYPE html>
<html>
    <head lang="en">
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <ul>
            <li class="item-"><a id='i1' href="link.html">first item</a></li>
            <li class="item-0"><a id='i2' href="llink.html">first2 item</a></li>
            <li class="item-1"><a href="llink2.html">second item<span>vv</span></a></li>
        </ul>
        <div><a href="llink2.html">second item</a></div>
    </body>
</html>
"""
response = HtmlResponse(url='http://example.com', body=html,encoding='utf-8')
obj = response.xpath('//a[@id]/text()').extract()
# 获取a标签的值
ext = response.xpath("//li[@class='item-1']/a/@href").extract()
print(obj)
print(ext)