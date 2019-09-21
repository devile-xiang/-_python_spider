# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MeifanSpider(CrawlSpider):
    name = 'meifan'
    allowed_domains = ['iesayoung.com']
    start_urls = ['http://iesayoung.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    # def parse_item(self, response):
    #     i = {}
    #     #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
    #     #i['name'] = response.xpath('//div[@id="name"]').extract()
    #     #i['description'] = response.xpath('//div[@id="description"]').extract()
    #     return i
    @property
    def start_requests(self):
        url="http://iesayoung.com/crm/login"
        date={"username":"lixiangqian", "password" : "95992959"}
        request=scrapy.FormRequest(url,formdata=date,callback=self.parse_page)
        print("正在登陆账号")
        yield request

    def parse_page(self, response):
        print("进入写html方法")

        with open('response.html','w',encoding='utf-8') as fp:
            fp.write(response.text)
