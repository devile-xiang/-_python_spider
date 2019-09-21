#encoding:utf-8
import requests
from lxml import etree
from urllib import request
import os
import re
import time

HEADERS={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'
}

def parse_page(url):
    response = requests.get(url,headers=HEADERS)
    text = response.text
    html = etree.HTML(text)
    imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
    time.sleep(0.5)
    for img in imgs:
        img_url = img.get('data-original')
        print(img_url)
        alt = img.get('alt')
        alt = re.sub(r'[\?？\.，。！!]', '', alt)
        suffix = os.path.splitext(img_url)[1]
        filename = alt + suffix
        print(filename)
        request.urlretrieve(img_url,'F:/untitled1/thread_dome/imgages/'+filename)


def main():
    for x in range(100):
        urls = 'http://www.doutula.com/photo/list/?page=%d'%x
        parse_page(urls)

if  __name__  ==  '__main__':
    main()