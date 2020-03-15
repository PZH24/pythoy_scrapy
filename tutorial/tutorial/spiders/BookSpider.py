# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?start=0&type=T']
    custom_settings = {'file_name': '/Users/dannihong/Documents/leetcode/scrapy_project/file/books.json'}  # spider上自定义配置信息

    def parse(self, response: HtmlResponse):  # 如何解析html;返回一个可迭代对象：利用yiled
        subjects = response.xpath('//li[@class="subject-item"]')
        items = []  # 如果用items=[]，最后函数要return items
        for subject in subjects:
            item = {} # 声明一个item，相当于一个字典，存放要爬取的数据
            title = subject.xpath('.//h2/a/text()').extract()
            item['title'] = title[0].strip()
            rate = subject.css('span.rating_nums::text').extract()
            item['rate'] = rate[0].strip()

            items.append(item)

        with open('book.json', 'w', encoding='utf8') as f:
            for item in items:
                f.write('{} {}\n'.format(item['title'], item['rate']))