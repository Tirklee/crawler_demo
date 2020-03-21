# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerDemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 序号
    seq_no = scrapy.Field()
    # 名称
    mv_name = scrapy.Field()
    # 介绍
    intduce = scrapy.Field()
    # 星级
    star = scrapy.Field()
    # 评论数
    commentnum = scrapy.Field()
    # 描述
    desc = scrapy.Field()
