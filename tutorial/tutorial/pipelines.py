# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 处理管道。
from scrapy import Spider
import json


class TutorialPipeline(object):

    def process_item(self, item, spider):
        # 对结果进行处理

        return item
# process_item(self, item, spider)  #
# item表示爬取的一个个数据，spider表示item的爬取者，每一个item处理都得调用。返回一个item对象，或者抛出DropItem异常，被丢弃的item对象将不会被pipeline组件处理；

# open_spider(self, spider)  # spider表示被开启的spider，调用一次

# close_spider(self, spider)  # spider表示被关闭的spider，调用一次

# __init__(self)  # spider创建实例时调用一次

# 定义一个接收yield的结果，对结果的处理


class FirstPipeline(object):
    def __int__(self):
        print('~~~~~~~~~~init~~~~~~~~~~')

    # 每一个item都会执行一次
    def process_item(self, item, spider: Spider):
        print('++++++++++')
        print(item)
        self.file.write('{},\n'.format(json.dumps(dict(item), ensure_ascii=False)))  # ensure_ascii=False 防止写入乱码。
        return item

    # 所有过程在起始的时候执行一次
    def open_spider(self, spider):
        print('==========open spider {}=========='.format(spider))
        # file_name = '/Users/dannihong/Documents/leetcode/scrapy_project/file/books.json'
        file_name = spider.settings['file_name']
        self.file = open(file_name, 'w', encoding='utf-8')
        self.file.write('[\n')

    # 所有过程结束的时候执行一次
    def close_spider(self, spider):
        print('==========close spider {}=========='.format(spider))
        self.file.write(']')
        self.file.close()
