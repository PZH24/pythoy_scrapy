# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import  Selector
from ..items import FirstProItem


class BookSpider(scrapy.Spider):
    # 存储链接。
    page_link = set()
    name = 'bookType'  # 爬虫名
    allowed_domains = ['douban.com']  # 爬虫爬取范围
    start_urls = [
        'https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?start=0&type=T']  # 起始url
    custom_settings = {
        'file_name': '/Users/pengzhihui/Desktop/opt/books.json'}  # 一般设置参数
    # rules = {
    #     'page': LinkExtractor(
    #         allow=r'^http://news.sohu.com/\d{8}/\w+.shtml')}

    # start_urls的是start_requests子方法
    # 通过函数进行对请求定制的初始化集合。
    # def start_requests(self):
    #
    #     for i in range(5230, 5133)[::-1]:
    #
    #         url = "http://news.sohu.com/guoneixinwen_" + str(i) + ".shtml"
    #
    #         self.page_link.add(url)
    #
    #         for url in self.page_link:
    #             yield self.make_requests_from_url(url)

    # make_requests_from_url()将被调用来创建Request对象
    # 下载器获取WebServer的response，parse解析响应的内容；输出items和requests
    # callback 函数可以执行回调，回调到某个函数的操作
    # scrapy.Request 新增请求地址

    def parse(self, response: HtmlResponse):
        # 如何解析html;返回一个可迭代对象：yield
        select = Selector(response)
        subjects = response.xpath('//li[@class="subject-item"]')
        lst = response.xpath(
            '//span[@class="next"]/a/@href').extract()
        items = []  # 如果用items=[]，最后函数要return items
        # for subject in subjects:
        #     item = FirstProItem()
        #     title = subject.xpath('.//h2/a/text()').extract()
        #     item['title'] = title[0].strip()
        #     rate = subject.css('span.rating_nums::text').extract()
        #     if rate:
        #         item['rate'] = rate[0].strip()
        #     yield item  # 返回一个可迭代对象生成器
        # if lst:
        #     lst = "https://book.douban.com" + lst
        #     self.page_link.add(lst)
        #     # 新增一个继续爬虫的链接
        #     yield scrapy.Request(lst, callback=self.parse)
        # BookSpider.start_urls.append('https://book.douban.com'+lst)


# 通过定义默认的请求，动态获取form表单上提交的数据FormRequest.from_response动态发表单请求。

