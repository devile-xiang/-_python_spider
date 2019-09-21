#encoding:utf-8

import requests
from lxml import etree
from queue import Queue
import threading
import csv

HEADERS={
    'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'
}




#生产者模式：
class Procuder(threading.Thread):
    def __init__(self,pageueue,textueue,*args,**kwargs):
        super(Procuder,self).__init__(*args,**kwargs)
        self.pageueue=pageueue
        self.textueue=textueue
    def run(self):
        while True:
            if self.pageueue.empty():
                break
            url=self.pageueue.get()
            self.gettext(url)

    def gettext(self,urls):
        print(urls)
        response = requests.get(urls,headers=HEADERS)
        text = response.text
        html = etree.HTML(text)
        # text=html.xpath("//h2/text()")
        title = html.xpath("//li[@class='col-xs-12 clearfix']//div[@class='lists_right_title']/text()")
        time=html.xpath("//li[@class='col-xs-12 clearfix']//span[@class='col-xs-12 col-sm-4']/text()")
        url=html.xpath("//li[@class='col-xs-12 clearfix']/a/@href")
        # self.img_queue.put((img_url, filename))
        page=[]

        for i in  range(len(title)):
            info=[
                'http://www.543zy.com'+url[i],
                 time[i],
                title[i],

            ]
            page.append(info)
            self.textueue.put((page))

            # print("链接:"+""+url[i]+"标题:"+title[i]+"时间:"+time[i]+"<br/>")
            # print("*"*10)
        # return  page

class Consumer(threading.Thread):
    def __init__(self,pageueue,textueue,*args,**kwargs):
        super(Consumer,self).__init__(*args,**kwargs)
        self.pageueue=pageueue
        self.textueue=textueue
    def run(self):
        while True:
            if self.pageueue.empty() and self.textueue.empty():
                break

            print("--------------正在写入数据--------------")
            headers = ['-----链接-----', '-----时间-----', '-----标题-----']
            page=self.textueue.get()
                # print(url[i])
            print(page)
            with open('test.csv', 'a', newline='', encoding='utf-8') as fp:
                writer = csv.writer(fp)
                writer.writerow(headers)
                writer.writerow([page])
                writer.writerow(['\n'])







def main():
    pageueue=Queue(100)
    textueue=Queue(2000)
    print('进入主方法')
    for i in range(1,11):
        urls='http://www.543zy.com/all/cate_alias/zhideyikan.html?page=%d'%i
        pageueue.put(urls)

    for x in range(5):
        t=Procuder(pageueue,textueue)
        t.start()
    for x in range(5):
        t=Consumer(pageueue,textueue)
        t.start()
    #
    #     gettext(urls)
    # print("--------------在main方法输出数据-------------------")
    # for i in page:
    #     print(i)
    # headers = ['-----链接-----', '-----时间-----', '-----标题-----']
    # with open('test.csv', 'w', newline='',encoding='utf-8') as fp:
    #     writer = csv.writer(fp)
    #     writer.writerow(headers)
    #     writer.writerows(page)





if __name__ == '__main__':
    main()