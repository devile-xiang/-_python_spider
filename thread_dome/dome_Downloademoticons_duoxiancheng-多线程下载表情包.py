#encoding:utf-8
import requests
from lxml import etree
from urllib import request
import os
import re
import time
from queue import Queue
import threading

HEADERS={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'
}
class Procuder(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Procuder,self).__init__(*args,**kwargs)
        self.page_queue=page_queue
        self.img_queue=img_queue
    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)


    def parse_page(self,url):
        response = requests.get(url,headers=HEADERS)
        text = response.text
        html = etree.HTML(text)
        imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
        time.sleep(0.5)
        for img in imgs:
            img_url = img.get('data-original')
            alt = img.get('alt')
            alt = re.sub(r'[\?？\.，。！!]', '', alt)
            suffix = os.path.splitext(img_url)[1]
            filename = alt + suffix
            # print(filename)
            # request.urlretrieve(img_url,'F:/untitled1/thread_dome/imgages/'+filename)
            self.img_queue.put((img_url,filename))
class Consumer(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Consumer,self).__init__(*args,**kwargs)
        self.page_queue=page_queue
        self.img_queue=img_queue
    def run(self):
        #解包操作
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_url,filename=self.img_queue.get()
            request.urlretrieve(img_url,'F:/untitled1/thread_dome/imgages/'+filename)
            print(filename+'下载完成！')

def main():
    page_queue=Queue(100)
    img_queue=Queue(1500)
    for x in range(6,100):
        urls = 'http://www.doutula.com/photo/list/?page=%d'%x
        page_queue.put(urls)
    for x in range(5):
        t=Procuder(page_queue,img_queue)
        t.start()
    for x in range(5):
        t=Consumer(page_queue,img_queue)
        t.start()

if  __name__  ==  '__main__':
    main()