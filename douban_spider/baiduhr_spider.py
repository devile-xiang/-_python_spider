
import requests
from lxml import etree
import codecs

PROXIES={
    'http':'115.218.208.41:9000'
}
HEADERS={
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
BASE_DOMAIN='https://hr.tencent.com/'

def get_ulr(home_url):
    # print(home_url)
    response=requests.get(home_url,headers=HEADERS,proxies=PROXIES)
    text=response.content.decode('utf-8')
    # print(text)
    html=etree.HTML(text)

    herf=html.xpath("//td/a[@target='_blank']/@href")
    urls = map(lambda url: BASE_DOMAIN + url , herf)

    return urls

    # for i in herf:
    #     print(i)


def parse_url(page_url):
    # print("这里是parse_url:")
    page_data={}
    pseponse=requests.get(page_url,headers=HEADERS,proxies=PROXIES)
    text=pseponse.content.decode('utf-8')
    # print(text)
    html=etree.HTML(text)
    #工作地点
    workaddress=html.xpath("//tr[@class='c bottomline']/td/text()")[0]
    page_data['workaddress']=workaddress
    #职位类别
    worktype=html.xpath("//tr[@class='c bottomline']/td/text()")[1]
    page_data['worktype']=worktype
    #招聘人数
    worlnum=html.xpath("//tr[@class='c bottomline']/td/text()")[2]
    page_data['worlnum']=worlnum
    # print(workaddress,worktype,worlnum)
    jobzz=html.xpath("//ul[@class='squareli']")[0]
    # print(jobzz)
    jobcontent=jobzz.xpath(".//li/text()")
    page_data['Jobcontent']=jobcontent

    jobyq = html.xpath("//ul[@class='squareli']")[1]
    # print(jobzz)
    jobdemand = jobyq.xpath(".//li/text()")
    page_data['jobdemand'] = jobdemand
    return  page_data

def spider():
    url="https://hr.tencent.com/position.php?keywords=python&tid=0&start={}#a"
    data=[]
    for i in  range(0,70):
        if (i%10==0):
            home_url=url.format(i)
            #要获取每一个页面的的url
            # print("spider:"+home_url)
            #正在获取，返回这一页的所有的内容页url
            page_ulr=get_ulr(home_url)
            for i in page_ulr:
                page_data=parse_url(i)
                data.append(page_data)
                print(page_data)

    f = codecs.open("python工作合集.txt", 'w', 'utf-8')
    # f.write(str(list))
    for k in data:
        f.write("\r\n\r\n------------------------------------华丽的分割线---------------------------\r\n\r\n\r\n\r\n")
        for i in k:

            f.write('工作地点:  '+k['workaddress'] + '\r\n\r\n')  # \r\n为换行符
            f.write('工作类型:  ' + k['worktype'] + '\r\n\r\n')  # \r\n为换行符
            f.write('招聘人数:  ' + k['worlnum'] + '\r\n\r\n')  # \r\n为换行符
            f.write('工作简介:  ' + str(k['Jobcontent']) + '\r\n\r\n')  # \r\n为换行符
            f.write('招聘要求:  ' + str(k['jobdemand']) + '\r\n\r\n\r\n\r\n')  # \r\n为换行符

    f.close()







if __name__ == '__main__':
    spider()