# -*- coding: utf-8 -*-
import scrapy
from urllib import request
from PIL import Image
import time
import urllib

class XinxiSpider(scrapy.Spider):
    name = 'xinxi'
    allowed_domains = ['1xinxi.cn']
    start_urls = ['http://web.1xinxi.cn/login.aspx']
    login_url="http://web.1xinxi.cn/login.aspx"

    def parse(self, response):
        time1 = int(time.time() * 1000)
        time2 = str(time1)
        fromdata={
            # '__EVENTTARGET':'',
            # '__EVENTARGUMENT':'',
            # '__VIEWSTATE':'/wEPDwUJNjUxODU5MTkyZGRT/QXKDRPVW6H7W27kqPMhKkSPkHMbW2K/TuxLt9ol3A==',
            # '__VIEWSTATEGENERATOR':'C2EE9ABB',
            # '__EVENTVALIDATION':'/wEdAAaGOYLzfr4UZ/QUkQHF8bkibSRY/Sd1Soe3bMMt3XikKYWDpeI41dtZo7urN/YwNwCFa3z02QmQnYFjj3wKxfjrop4oRunf14dz2Zt2+QKDEOI1Eb1eJVmFgpRa0agX9Ips5eKII16Xw6QPVmIeO7K0KsEcxMoRvxrTDBGCjsjUvg==',
            'txtLoginName':'18523555617',
            'txtLoginPwd':'1999418xby',
            'btnLogin':''
        }

        title=response.xpath("//title/text()").get()
        print("爬取页面的title%s"%title)
        yzmimgurl=response.xpath('//img[@class="login_img"]/@src').get()
        print("未拼接验证码地址：%s"%yzmimgurl)
        yzmimgurl = "http://web.1xinxi.cn/" + yzmimgurl+"?now="+time2
        print("已拼接验证码地址：%s" % yzmimgurl)
        captcha=self.regonize_captcha(yzmimgurl)
        fromdata['txtCode']=captcha
        yield scrapy.FormRequest(url=self.login_url,formdata=fromdata,callback=self.parse_after_login)

    def parse_after_login(self,response):
        title=response.xpath("//title/text()").get()
        print(title)
        now_url=response.url
        print("当前的链接是%s"%now_url)
        bodytext=response.xpath("//html/text()").get()
        print("="*50)
        print(bodytext)


    def regonize_captcha(self,img_url):
        #旧代码
        request.urlretrieve(img_url,'captcha.png')
        image1=Image.open('captcha.png')
        image1.show()
        captcha=input('亲输入验证码:')

        # captcha = response.xpath("//img[@class='login_img']/@src").extract()
        # if len(captcha[0])>0:
        #     request.urlretrieve(captcha[0],filename="captcha.jpg")
        #     image1=Image.open("captcha.jpg")
        #     image1.show()
        #     captcha_value = input('查看captcha.png,有验证码请输入:')
        #





        return captcha
