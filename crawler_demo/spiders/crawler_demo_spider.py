# -*- coding: utf-8 -*-
import scrapy
from crawler_demo.items import CrawlerDemoItem

class CrawlerDemoSpiderSpider(scrapy.Spider):
    name = 'crawler_demo_spider'
    allowed_domains = ['movie.douban.com']
    # 入口url扔进调度器中
    start_urls = ['https://movie.douban.com/top250']

    # 默认的解析方法
    def parse(self, response):
        # 循环电影的条目
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for i_item in movie_list:
            # item文件导入电影条目
            crawler_item = CrawlerDemoItem()
            # 详细的解析每一行数据
            crawler_item['seq_no'] = i_item.xpath(".//div[@class='item']//em/text()").extract_first()
            crawler_item['mv_name'] = i_item.xpath(
                ".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()
            # 处理多行数据
            content = i_item.xpath(".//div[@class='info']//div[@class='bd']/p[1]/text()").extract()
            for i_content in content:
                content_s = "".join(i_content.split())
                crawler_item['intduce'] = content_s
            crawler_item['star'] = i_item.xpath(".//span[@class='rating_num']/text()").extract_first()
            crawler_item['commentnum'] = i_item.xpath(".//div[@class='star']//span[4]/text()").extract_first()
            crawler_item['desc'] = i_item.xpath(".//p[@class='quote']/span/text()").extract_first()
            # yield到pipeline,settings中需要启用，否则无法存储数据
            yield crawler_item

        nextLink = response.xpath('//span[@class="next"]/link/@href').extract()
        # 第10页是最后一页，没有下一页的链接
        if nextLink:
            nextLink = nextLink[0]
            print(nextLink)
            yield scrapy.Request('https://movie.douban.com/top250' + nextLink, callback=self.parse)
            # # 递归将下一页的地址传给这个函数自己，在进行爬取
