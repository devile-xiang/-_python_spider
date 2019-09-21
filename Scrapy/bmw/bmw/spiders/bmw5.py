# -*- coding: utf-8 -*-
import scrapy
from urllib import request

class Bmw5Spider(scrapy.Spider):
    name = 'bmw5'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    def parse(self, response):
        # 返回的是selectorList
        uiboxs=response.xpath('//div[@class="listing fn-mt"]/div["project"]')
        print(uiboxs)
        text=uiboxs[1].xpath('//span[@class="athm-title__item"]/text()').getall()
        print(text[1])
        print(text[2])
        urls=uiboxs[1].xpath('//ul/li/a/img/@src').getall()
        print(urls)

        for i ,url in enumerate(urls):
            if url[1]=="/":
                url=url[3:]
                print("刚刚删除完//的URL：%s"%url)
            print("for 已删除//的URL:%s"%url)
            l=str(i)
            # print(type(l))
            assert isinstance(url, object)
            request.urlretrieve(url,'tu.jpg')







