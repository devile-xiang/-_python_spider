#encoding:GBK

import requests
from lxml import etree
import codecs

#��ȡ����ַ
BASE_DOMAIN="http://www.aiqqzy.com/"
HEADERS = {
    'User_Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36',
    'Referer': 'https://accounts.douban.com/register'
}
PROXIES={
    "http": "106.112.166.110:16269"


}

def get_page_url(url):
    response=requests.get(url,headers=HEADERS,proxies=PROXIES)
    text=response.content.decode('gbk')

    # print(text),text�������������Ѿ��Ѿ������˵�htmlҳ��
    html=etree.HTML(text)

    urls=html.xpath("//a[@style='color:;font-weight:bold;']/@href")
    urls=map(lambda url:BASE_DOMAIN+url,urls)
    # urls = map(lambda url: BASE_DOMAIN + url, urls)
    return urls

def parse_url(url):
    page_data={}
    response = requests.get(url,headers=HEADERS,proxies=PROXIES)
    text=response.content.decode('gbk')
    html=etree.HTML(text)
    #���±���
    title=html.xpath("//h2[@class='post-title']/text()")
    page_data['title']=title
    #���·���ʱ��
    releasetime=html.xpath("//span['ptime']/text()")[0]
    # print(releasetime)
    page_data['releasetime']=releasetime
    #�������ͣ�
    type=html.xpath("//a[@rel='category tag']/text()")
    # print(type)
    page_data['type']=type
    imgs=[]
    imgs=html.xpath("//div[@id='arctext']/p[@style='text-align:center;']//img/@src")
    img=[]
    for i in imgs:
        img.append(BASE_DOMAIN+i)
        # print(i)
    page_data['img']=img
    download=html.xpath("//span[@style='color:#E53333;']/text()")
    # print(download)
    page_data['download']=download

    return page_data

def spider():
    base_url="http://www.aiqqzy.com/i_wz_51122_Page{}.html"
    #������ݺϼ�
    data=[]
    for x in range(1,8):
        #��·���е�url������ֵ
        url = base_url.format(x)
        # print(url)
        #��ȡÿһ������ҳҳ�����ַ,����ڼ�ҳ��������һҳ����������ҳ��ַ
        page_url=get_page_url(url)
        for i in page_url:
            page_data=parse_url(i)
            data.append(page_data)
            print(page_data)


    s=u'�����ϼ�:\r\n'

    f = codecs.open("dome1.py.txt", 'w', 'utf-8')

    f.write(s)
    # f.write(str(list))
    for i in data:
        f.write("------------------------------------�����ķָ���---------------------------\r\n")
        f.write(str(i) + '\r\n')  # \r\nΪ���з�

    f.close()
    # print(data)

if __name__ == '__main__':
    spider()


