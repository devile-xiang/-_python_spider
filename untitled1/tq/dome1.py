#encoding:utf-8

from bs4 import BeautifulSoup
import requests
from pyecharts import Bar

ALL_DATA=[]
PROXIES={
    "https":"122.114.31.177:808"
}
def parse_page(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

    }
    respones=requests.get(url,headers=headers,proxies=PROXIES)
    text=respones.content.decode('utf-8')
    soup=BeautifulSoup(text,'lxml')
    # soup = BeautifulSoup(text, 'html5lib')
    conMidtab=soup.find('div',class_='conMidtab')
    # print(conMidtab)

    tables=soup.find_all('table')
    for i in tables:
        trs=i.find_all("tr")[2:]
        for index,tr in enumerate(trs):
            tds=tr.find_all('td')
            city_td=tds[0]
            if index==0:
                city_td=tds[1]
            city=city_td.get_text().strip()
            temp_td=tds[-2]
            min_temp=temp_td.get_text().strip()
            ALL_DATA.append({"city":city,"min_temp":int(min_temp)})
            # print({"city:":city,"temp:":temp})

def main():

    # url = "http://www.weather.com.cn/textFC/hb.shtml"
    # url = "http://www.weather.com.cn/textFC/db.shtml"
    # url = "http://www.weather.com.cn/textFC/hd.shtml"
    # url = "http://www.weather.com.cn/textFC/hz.shtml"
    # url = "http://www.weather.com.cn/textFC/hn.shtml"
    # url = "http://www.weather.com.cn/textFC/xb.shtml"
    # url = "http://www.weather.com.cn/textFC/xn.shtml"
    # url = "http://www.weather.com.cn/textFC/gat.shtml"


    urls=[
        'http://www.weather.com.cn/textFC/hb.shtml',
        # 'http://www.weather.com.cn/textFC/db.shtml',
        # 'http://www.weather.com.cn/textFC/hd.shtml',
        # 'http://www.weather.com.cn/textFC/hz.shtml',
        # 'http://www.weather.com.cn/textFC/hn.shtml',
        # 'http://www.weather.com.cn/textFC/xb.shtml',
        # 'http://www.weather.com.cn/textFC/xn.shtml',
        # 'http://www.weather.com.cn/textFC/gat.shtml'

    ]
    for url in urls:
        parse_page(url)
    #分析数据
    #根据最低气温进行排序

    # ALL_DATA.sort(key=lambda data:data['min_temp'])
    print("最低气温排序")
    ALL_DATA.sort(key=lambda data:data['min_temp'])
    data=ALL_DATA[0:10]
    chart=Bar("中国最低气温排行榜")
    cities=list(map(lambda x:x['city'] ,data))
    temps=list(map(lambda x:x['min_temp'],data))
    chart.add('',cities,temps)
    chart.render('temp.html')
if __name__ == '__main__':
    main()

