# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import DingdiantextItem



class DingdianSpider(CrawlSpider):
    name = 'dingdian'
    allowed_domains = ['www.23us.so']
    start_urls = ['https://www.23us.so/list/6_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'.+list/6_\d+.html'), follow=False),
        Rule(LinkExtractor(allow=".+xiaoshuo/\d+.html"),callback="parse_item",follow=False)
    )

    def parse_item(self, response):
        url=response.url
        title=response.xpath("//h1/text()").get()
        type=response.xpath("//td/a/text()").get()
        print("当前爬取的连接是%s"%url)
        print("当前连接的标题是%s"%title)
        print("当前连接的小说类别:%s"%type)

        item=DingdiantextItem(title=title,type=type,url=url)

        yield item









        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
