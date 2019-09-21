

import requests
from lxml import etree
import re
import codecs
import csv
import pandas as pd
PROXIES={
    # "http": "175.161.12.142:9000"
}
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'}

def get_content(url):
   newurl="http://www.ltxs888.com"+url
   print(newurl)
   respons=requests.get(newurl,headers=HEADERS,proxies=PROXIES)
   text=respons.content.decode('gbk','ignore')
   #上，如果gbk解析不了，就跳过当前非法字符
   html=etree.HTML(text)
   title=html.xpath("//div[@id='srcbox']/div/a[3]/text()")
   print("书名：",title)
   chappter=html.xpath("//h1[@id='title']/text()")
   print("章节：",chappter)
   info=html.xpath("//div[@id='content']/text()")

   info[-1]=info[-1].replace('( 都市猎艳：少妇俱乐部  http://www.ltxs888.com/0/3/ 移动版地址wap.ltxs888.com )', '')
   return info


   # infos=info.strip()
   # print(infos)




   # for index,info in enumerate(infos):
   #     if infos.startswith("("):
   #         text = parse_info(info, "(")
   #         if text.startswith("("):
   #             break
   #
   #
   #
   # print(text)


def parse_info(info,rule):
    return info.replace(rule,"").strip()
def page(url):
    # print(url)
    respons = requests.get(url, headers=HEADERS, proxies=PROXIES)
    text = respons.content.decode('gbk')
    html = etree.HTML(text)
    atexts=html.xpath("//ul[@class='ListRow']/li/a/text()")
    hrefs = html.xpath("//ul[@class='ListRow']/li/a/@href")
    return atexts,hrefs
def get_url(weburl):

    respons=requests.get(url,headers=HEADERS,proxies=PROXIES)
    text=respons.content.decode('gbk')
    html=etree.HTML(text)
    ph=html.xpath("//ul[@class='ranking-list']/li/a/text()")
    texturl=html.xpath("//ul[@class='ranking-list']/li/a/@href")
    return ph,texturl




if __name__ == '__main__':
    url="http://www.ltxs888.com/"
    ph,page_url=get_url(url)
    #ph文章名
    data=""
    for i in range(len(url)):
        atext,hrefs=page(page_url[i])
        #atext,章节
        # print(atext)
        for k in range(len(hrefs)-1):
            if(len(hrefs[k])>25):
                break
            content=get_content(hrefs[k])
            for Y in content:
                data = data + Y
            print(ph[1])
            print(atext[1])
            print(data)
            dataframe = pd.DataFrame({'bookname':ph[i], 'pagename':atext[k],'content':data},index=[0])

            # 将DataFrame存储为csv,index表示是否显示行名，default=True
            dataframe.to_csv("data.csv", index=True, sep=',')

    # # 字典中的key值即为csv中列名
    # for i in range(len(data)):
    #     dataframe = pd.DataFrame({'a_name':ph[1], 'b_name':atext[1],'content[i]':data})
    #
    #     # 将DataFrame存储为csv,index表示是否显示行名，default=True
    #     dataframe.to_csv("test.csv", index=False, sep=',')











