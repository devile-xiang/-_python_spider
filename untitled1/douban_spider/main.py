#encoding:utf-8

import requests
from lxml import etree
#.1.将目标网站的页面抓取下来

headers={
    'User_Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36',
    'Referer':'https://accounts.douban.com/register'
}
url='https://movie.douban.com/cinema/nowplaying/chongqing/'

response=requests.get(url,headers=headers)
# print(response.text)
#response.text,返回的是一个解码后的，字符串，是str(unicode)类型
#response.content,返回的是一个原生的字符串，就是从网页上抓取下来的，没有经过处理的
# 字符串，就是nyte类型

text=response.text

#2.将抓取下来的数据根绝一定的规则进行提取
movies=[]

html=etree.HTML(text)

ul=html.xpath("//ul[@class='lists']")[0]
# print(etree.tostring(ul,encoding='utf-8').decode('utf-8'))

lis=ul.xpath("./li")
for li in lis:
    # print(etree.tostring(li,encoding='utf-8').decode('utf-8'))
    title=li.xpath("@data-title")[0]
    score=li.xpath("@data-score")[0]
    duration=li.xpath("@data-duration")[0]
    region=li.xpath("@data-region")[0]
    director=li.xpath("@data-director")[0]
    actors=li.xpath("@data-actors")[0]
    thumbnail=li.xpath(".//img/@src")
    movie={
        'title':title,
        'score':score,
        'director':director,
        'region':region,
        'director':director,
        'actors':actors,
        'thumbnail':thumbnail,
    }
    movies.append(movie)

# print(movies)

print("正在热映：")
for i in range(len(movies)):
    print(movies[i])

moviej=[]
ul=html.xpath("//ul[@class='lists']")[1]
# print(etree.tostring(ul,encoding='utf-8').decode('utf-8'))

lis=ul.xpath("./li")
print(lis)
for li in lis:
    # print(etree.tostring(li,encoding='utf-8').decode('utf-8'))
    title=li.xpath("@data-title")[0]
    duration=li.xpath("@data-duration")[0]
    region=li.xpath("@data-region")[0]
    director=li.xpath("@data-director")[0]
    actors=li.xpath("@data-actors")[0]
    thumbnail=li.xpath(".//img/@src")
    movie={
        'title':title,
        'director':director,
        'region':region,
        'director':director,
        'actors':actors,
        'thumbnail':thumbnail,
    }
    moviej.append(movie)

# print(movies)
print("即将上映：")
for i in range(len(moviej)):
    print(moviej[i])