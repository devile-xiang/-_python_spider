#encoding:GBK

import requests
from lxml import etree
import time

BASE_DOMAIN='http://www.ygdy8.net'
PROXY={
    'http': '39.137.77.68:80'
}
HEADERS = {
    'User_Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36',
    'Referer': 'https://accounts.douban.com/register'
}
def get_detail_urls(url):


    response = requests.get(url=url, headers=HEADERS)
    # 下载时就设置编码类型
    text = response.content.decode('gbk')

    html = etree.HTML(text)
    urls = html.xpath("..//a[@class='ulink']/@href")
    #每一项执行添加域名的操作
    urls=map(lambda url:BASE_DOMAIN+url,urls)
    #爬取电影天堂2
    # for i in urls:
    #     print(BASE_DOMAIN + i)
    #
    return urls
def parse_detail_page(url):
    movie={}
    response=requests.get(url,headers=HEADERS)
    text=response.content.decode('gbk')
    html=etree.HTML(text)
    title=html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")
    movie['title']=title
    zoomE=html.xpath("//div[@id='Zoom']")[0]
    imgs=zoomE.xpath("//img/@src")
    cover=imgs[0]
    screensheet=imgs[1]
    movie['cover']=cover
    movie['screensheet']=screensheet

    def parse_info(info,rule):
        return info.replace(rule,"").strip()

    infos=zoomE.xpath(".//text()")
    #enumerate,遍历并提供下标
    for index,info in enumerate(infos):
        #获取列表中从什么开始
        if info.startswith("◎年　　代"):
            info=parse_info(info,"◎年　　代")
            movie['year']=info
        elif info.startswith("◎产　　地"):
            info =parse_info(info,"◎产　　地")
            movie['country']=info
        elif info.startswith("◎类　　别"):
            info = parse_info(info,"◎类　　别")
            movie['category']=info
        elif info.startswith("◎豆瓣评分"):
            info=parse_info(info,"◎豆瓣评分")
            movie['douban_rating']=info
        elif info.startswith("◎片　　长"):
            info=parse_info(info,"◎片　　长")
            movie['duration']=info
        elif info.startswith("◎导　　演"):
            info=parse_info(info,"◎导　　演")
            movie['director']=info
        elif info.startswith("◎主　　演"):
            info = parse_info(info, "◎主　　演")
            actors=[info]
            for x in range(index+1,len(infos)):
                actor=infos[x].strip()
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            movie['actors']=actors
        elif info.startswith("◎简　　介"):
            info=parse_info(info,"◎简　　介")
            for x in range(index+1,len(infos)):
                proflie=infos[x].strip()
                if proflie.startswith("◎获奖情况"):
                    break
            movie['proflie']=proflie
    download_url=zoomE.xpath("//td[@bgcolor='#fdfddf']/a/@href")
    movie['download_url']=download_url

    return movie


def spider():
    base_url="http://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html"
    #获取总共有七页
    movies=[]
    for x in range(1,8):
        url=base_url.format(x)
        detail_urls=get_detail_urls(url)
        #是用来遍历一页当中所有电影详情
        for datail_url in detail_urls:
            movie=parse_detail_page(datail_url)
            movies.append(movie)
            print(movie)
            time.sleep(1)

    # print(movies)
if __name__ == '__main__':
    spider()

