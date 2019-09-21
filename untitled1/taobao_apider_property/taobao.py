#encoding:utf-8

import time,datetime
import requests
from lxml import etree
from queue import Queue
import threading
import json
import time
import xlwt

HEADERS = {
    'Referer': 'https://sf.taobao.com/item_list.htm?spm=a213w.7398504.filter.14.5b2335d6Q0QKcU&category=50025969&city=&province=%D5%E3%BD%AD&sorder=1&auction_start_seg=-1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'
}

def get_Total():
    TotalUrl = "https://sf.taobao.com/item_list.htm?spm=a213w.7398504.filter.14.5b2335d6Q0QKcU&category=50025969&city=&province=%D5%E3%BD%AD&sorder=1&auction_start_seg=-1"
    response=requests.get(url=TotalUrl,headers=HEADERS)
    text=response.content
    html=etree.HTML(text)
    Totalpage=html.xpath('//em[@class="page-total"]/text()')
    print("即将开始总共有%s页" % Totalpage[0])
    return Totalpage[0]
# class Producer(threading.Thread):
#     def __init__(self,page_url_queue,House_property_queue,*args,**kwargs):
#         super(Producer,self).__init__(*args,**kwargs)
#         self.page_url_queue=page_url_queue
#         self.House_property_queue=House_property_queue
#     def run(self):
#         while True:
#             if self.page_url_queue.empty():
#                 break
#             url=self.page_url_queue.get()
#             self.Parse_page(url)

def Parse_page(url):
        data=[]
        response=requests.get(url=url,headers=HEADERS)
        text=response.text
        html=etree.HTML(text)

        jsondate=html.xpath('//script[@id="sf-item-list-data"]/text()')
        date=jsondate[0].strip().replace("\n", "")
        # print("*"*10+"页面获取的json数据"+"*"*10)
        # print("未解析的数据%s" % date)
        dataa=json.loads(date)['data']
        # print("解析了的数据%s"%dataa)
        print(len(dataa))
        for i in dataa:
            # print("正在写入数据:")
            # print(i)
            # print(i)
            data.append(i)
            print(i)
        return data

# class Consumption1(threading.Thread):
#     def __init__(self,page_url_queue,House_property_queue,numqueue,*args,**kwargs):
#         super(Consumption1,self).__init__(*args,**kwargs)
#         self.page_url_queue=page_url_queue
#         self.House_property_queue=House_property_queue
#         self.numqueue=numqueue
#
#     def run(self):
#
def seve_xls(data):
            book=xlwt.Workbook(encoding='utf-8',style_compression=0)
            sheet=book.add_sheet('房地产',cell_overwrite_ok=False)
            # print("写入数据：%s"%data)
            sheet.write(0, 0, "数据如下")
            sheet.write(0, 1, "阿里巴巴数据库的房屋编号")
            sheet.write(0, 2,"地址")
            sheet.write(0,3, "起拍价")
            sheet.write(0, 4, "开拍时间")
            sheet.write(0, 5, "是否支持信用贷款")

            for i,row in enumerate(data):
                print("写入数据：" + "x" * 30)
                # 阿里巴巴编号
                i=i+1
                print(i)
                print(row['title'])
                # print(data[i][j]['title'])
                sheet.write(i,1,row['id'])
                #房屋地址
                sheet.write(i,2,row['title'])
                #初始价格
                sheet.write(i,3,row['initialPrice'])

                #开始时间
                timeArray = time.localtime(row['timeToStart'])
                otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
                sheet.write(i,4,otherStyleTime)
                #是否支持信用贷款
                if(row['supportOrgLoan']!=0):
                    sheet.write(i,5,'支持信用贷款')
                else:
                    sheet.write(i, 5,'不支持支持信用贷款')

            book.save('test.xls')
            print("数据存储完成...")










def main():

    Totalpage=get_Total()
    Totalpage=int(Totalpage)
    # print(Totalpage)
    # print(type(Totalpage))
    #要解析的页面的路径
    # page_url_queue=Queue(500)
    # #解析完路径，存储好的数据
    # House_property_queue=Queue(9999999999999999)
    data=[]
    for i in range(1,Totalpage):
       page_url="https://sf.taobao.com/item_list.htm?spm=a213w.7398504.pagination.2.50d8293dsorXQ2&category=50025969&province=%%D5%%E3%%BD%%AD&sorder=1&auction_start_seg=-1&page=%d"%i
       a=Parse_page(page_url)

       for i in a:
           data.append(i)
    # for i in range(2):
    #     t1=Producer(page_url_queue,House_property_queue)
    #     t1.start()
    #     time.sleep(3)

    print("*"*50)
    print(data)
    seve_xls(data)
    # seve_xls(House_property_queue,page_url)


if __name__ == '__main__':
    main()




