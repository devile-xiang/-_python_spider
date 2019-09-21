# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    #allowed_domains:这个不不要加http:
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=1&page=1']

    rules = (
        # follow，爬取了第一页，继续跟进爬取后面页面爬去出来满足条件得链接
        Rule(LinkExtractor(allow=r'.+mod=list&catid=1&page=\d'), follow=False),
        Rule(LinkExtractor(allow=r".+article-.+\.html"),callback="parse",follow=False)
    )


    def parse(self, response):
        body=response.xpath("//body").get()
        url=response.url
        print("这次我们爬去的页面是%s"%url)

        # print("网页代码如下")
        print(body)


        url=response.xpath("//a/@href").getall()
        for i in url:
            print(i)


        print("获取页面")
        # print("现在你已经进入parse_detail（）方法")
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()

        # title=response.xpath('//h1[@class="ph"]/text()').get()

        # print("现在爬取页面的title%s"%title)


        # return i
