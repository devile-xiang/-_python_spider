# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WeisuenSpider(CrawlSpider):
    name = 'weisuen'
    allowed_domains = ['bbs.classic023.com']
    start_urls = ['http://bbs.classic023.com/forum-85-1.html']

    rules = (
        Rule(LinkExtractor(allow=r'forum-85-.+\.html'),follow=True),
        Rule(LinkExtractor(allow=r"thread-.+\.html"),callback="parse", follow=False)
    )

    def parse(self, response):
        url=response.url
        print(url)
        html=response.xpath("//html").get()
        print(html)

        # html=response.xpath("//html").get()
        # print(html)
        # print("现在已经进入页面分析阶段")
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # url=response.url
        # print("这次我们爬取得连接是%s"%url)

        title=response.xpath('//a/@href').getall()
        print("当前页面的标题是：%s"%title)



        return i
