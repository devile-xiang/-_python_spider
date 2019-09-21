# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class EnergyspiderSpider(CrawlSpider):
    name = 'energyspider'
    allowed_domains = ['www.china5e.com']
    start_urls = ['https://www.china5e.com/new-energy/clean-energy-vehicles/index_1.html']

    rules = (
        #分类页面的匹配链接
        Rule(LinkExtractor(allow=r'.+/clean-energy-vehicles/index_\d+.html'),callback='parse_index', follow=True),
        #匹配详细页面的链接
        Rule(LinkExtractor(allow=r'https://www.china5e.com/news/news-\d+-1.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        print("-"*10+"进入页面编译方法！！"+"-"*10)
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()

        url=response.url

        title=response.xpath("//h1/text()").get().strip()
        print("当前爬取页面的标题是%s"%title)


        return i
    def parse_index(self, response):
        url=response.url
        print(url)