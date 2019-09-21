# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):

    name = 'douban'
    allowed_domains = ['douban.com']
    # start_urls = ['https://accounts.douban.com/login'].
    start_urls = ['https://www.douban.com/about']


    def parse(self, response):
        print("现在进入了返回页面的解析方法！")
        formdata={
            'source':'None',
            'redir':'https://www.douban.com/',
            'form_email':'18523555617',
            'form_password':'1999418xby',
            'login':'登录'
        }



        print("="*30)
        a=response.xpath("//html").get()
        print(a)
        # captcha_image=response.xpath('//img[@id="captcha_image"]/@src')
        text=response.xpath("//label/text()").get()
        print(text)
        # print(captcha_image)
