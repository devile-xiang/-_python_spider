#encoding:GBK

import requests
from lxml import etree
import codecs

#爬取得网址
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

    # print(text),text，是下载下来已经已经解码了的html页面
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
    #文章标题
    title=html.xpath("//h2[@class='post-title']/text()")
    page_data['title']=title
    #文章发布时间
    releasetime=html.xpath("//span['ptime']/text()")[0]
    # print(releasetime)
    page_data['releasetime']=releasetime
    #文章类型：
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
    #最后内容合集
    data=[]
    for x in range(1,8):
        #向路径中的url变量赋值
        url = base_url.format(x)
        # print(url)
        #获取每一个内容页页面的网址,传入第几页，返回这一页的所有内容页网址
        page_url=get_page_url(url)
        for i in page_url:
            page_data=parse_url(i)
            data.append(page_data)
            print(page_data)


    s=u'技术合集:\r\n'

    f = codecs.open("dome1.py.txt", 'w', 'utf-8')

    f.write(s)
    # f.write(str(list))
    for i in data:
        f.write("------------------------------------华丽的分割线---------------------------\r\n")
        f.write(str(i) + '\r\n')  # \r\n为换行符

    f.close()
    # print(data)

if __name__ == '__main__':
    spider()


