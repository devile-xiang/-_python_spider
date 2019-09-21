#encoding:utf-8

from selenium import webdriver
from lxml import etree
import time

class Lagouspider(object):
    driver_path=r"F:\ruanjian\pythonapp\2.41.exe"
    def __init__(self):
        self.driver=webdriver.Chrome(
            executable_path=Lagouspider.driver_path
        )
        self.url='https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        self.workSeduction=[]
    def run(self):
        while True:
            self.driver.get(self.url)
            # page_source 获取到当前页面的页面代码
            source = self.driver.page_source
            self.parse_list_page(source)
            time.sleep(2)
            next_bth = self.driver.find_element_by_xpath('//div[@class="pager_container"]/span[last()]')
            if "pager_next_disabled" in next_bth.get_attribute("class"):
                break
            else:
                next_bth.click()
    def parse_list_page(self,sourcr):
        html=etree.HTML(sourcr)
        links=html.xpath('//a[@class="position_link"]/@href')
        for link in links:
            self.request_detail_page(link)
            time.sleep(1)
    def request_detail_page(self,url):
        #打开新的窗口
        self.driver.execute_script("window.open('%s')"% url)
        #切换到新打开的页面
        self.driver.switch_to.window(self.driver.window_handles[1])
        source=self.driver.page_source
        self.parse_detail_page(source)

        #关闭当前这个详情页
        self.driver.close()
        #继续切换回职位页
        self.driver.switch_to.window(self.driver.window_handles[0])
    def parse_detail_page(self,source):
        #解析页面
        html=etree.HTML(source)
        #爬起页面
        Seduction=html.xpath('//dd[@class="job-advantage"]/p/text()')
        company_name=html.xpath('//h2[@class="fl"]/text()')[0].strip()
        print(Seduction)
        print("当前公司是：%s"%company_name)
        #插入数据
        self.workSeduction.append(Seduction)

if __name__ == '__main__':
    spider=Lagouspider()
    spider.run()