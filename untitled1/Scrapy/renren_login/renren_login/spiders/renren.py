# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    # def parse(self, response):
    #     pass
    def start_requests(self):
        url="http://www.renren.com/PLogin.do"
        data={"email":"18523555617","passworld":"1999418xby"}
        request=scrapy.FormRequest(url,formdata=data,
                                   callback=self.parse_page)
        print("正在登陆密码账号")
        yield request


    def parse_page(self,response):

        body=response.xpath("//html").get()
        print(body)


        print("进入写html方法")
        with open('response.html','w',
                  encoding='utf-8') as fp:
            fp.write(response.text)


