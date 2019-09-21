#encoding:utf-8


from lxml import etree

import requests


def main():

    headers={
        'Upgrade-Insecure-Requests':'1',
        'Referer':'https://www.23us.so/',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'
    }


    url="http://bbs.classic023.com/forum-85-1.html"

    respons=requests.get(url=url,headers=headers)

    # text=respons.content.decode('gbk','ignore')

    html=etree.HTML(respons.content)

    body=html.xpath("//a/@href")
    print(body)






    print("你好")

if __name__ == '__main__':
    main()