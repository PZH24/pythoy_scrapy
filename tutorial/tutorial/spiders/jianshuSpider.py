# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JianshuspiderSpider(CrawlSpider):
    name = 'jianshuSpider'  # 模块启动的名称
    allowed_domains = ['jianshu.com']  # 真实的名字
    start_urls = ['http://jianshu.com/']  # 爬虫的地址
    # 定义个爬取url的规则
    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        return item
