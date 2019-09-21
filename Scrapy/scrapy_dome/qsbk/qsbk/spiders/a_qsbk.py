# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse

from scrapy.selector.unified import SelectorList
from lxml import etree

class AQsbkSpider(scrapy.Spider):
    name = '_qsbk'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    base_domin="https://www.qiushibaike.com/text/page/"
    page=2
    def parse(self, response):
        # danzidivs =response.xpath('//div[@id="content-left"]/div')

        body=response.xpath("//html").get()
        print(body)




        danzidivs =response.xpath('//article')
        print(danzidivs)


        for danzidiv in danzidivs:
            # #头像：
            # avatar=danzidiv.xpath('header/a[@class="avatar"]/@background-image')
            # print("头像地址是%s"%avatar)
            #获取用户的昵称
            username=danzidiv.xpath('header/a[@class="username"]/text()').get().strip()
            # print("他的昵称是%s"%username)
            #获取用户的年龄
            age=danzidiv.xpath('header/div/i[@class="age"]/text()')
            # print("年龄是：%s"%age)
            #获取笑话内容
            #getall的意思是获取所有内容成为字符串
            content=danzidiv.xpath('a//text()').getall()
            #然后用join拼接成一句话，strip() 去除中间的空格和换行符
            content="".join(content).strip()
            duanzi={
                "username":username,
                "content":content
            }
            # print("yield:返回的数据"+"="*50)
            yield duanzi
            # next_url=danzidivs.xpath('//ul[@lcass="pagination"]/li[lase()]/a/@href').get()
            # print("怕取出来的下一页：%s"%next_url)
            # # print(next_url)

            # if self.page<14:
            #     next_url=self.page
            #     next_url=str(next_url)
            #     self.page=self.page+1
            a=self.base_domin+"2"+"/"
            print("我们要爬取得连接是：%s"%a)
            # yield scrapy.Request(a,callback=self.parse())
            # else:
            #     return
