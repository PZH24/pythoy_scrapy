# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class taobaoItem(scrapy.Item):
    pass


class FirstItem(scrapy.Item):
    pass


# 通过 yield 生成迭代器返回到对应的item当中
class FirstProItem(scrapy.Item):
    title = scrapy.Field()  # 存放标题
    rate = scrapy.Field()  # 存放评分
    pass