#encoding:utf-8


from selenium import webdriver
from lxml import etree
import time

class Spider(object):
    driver_path = r"F:\ruanjian\pythonapp\2.41.exe"
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path=Spider.driver_path)
        self.url="https://www.zhipin.com/c101040100/?query=php&page=1&ka=page-1"
        self.workdata=[]
    def run(self):
        while True:
            self.driver.get(self.url)
            soruce=self.driver.page_source

            self.pare_list_page(soruce)
            next_bth=self.driver.find_element_by_xpath('//a[@ka="page-next"]')
            if "next disabled" in next_bth.get_attribute("class"):
                break;
            else:
                next_bth.click()
        return self.workdata
    def pare_list_page(self,soruce):
        html=etree.HTML(soruce)
        links=html.xpath('//div[@class="info-primary"]/h3/a/@href')
        for i in links:
            page_url="https://www.zhipin.com/%s"% i
            self.parse_page(page_url)
            time.sleep(1)

    def parse_page(self,page_url):
        print(page_url)
        self.driver.execute_script("window.open('%s')" % page_url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        soruce=self.driver.page_source
        self.get_text(soruce)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])


    def get_text(self,soruce):
        html=etree.HTML(soruce)
        #获取工资
        wages=html.xpath('//span[@class="badge"]/text()')
        #获取招聘公司
        company_name=html.xpath('//a[@class="job-detail-company"]/text()')
        #公司要求：
        city=html.xpath('//div[@class="info-primary"]/p/text()')
        #职位职责：
        jobduties=html.xpath('//div[@class="job-sec"]/div[@class="text"]/text()')
        #公司描述：
        company_information=html.xpath('//div[@class="job-sec company-info"]/div[@class="text"]/text()')
        position={
            'wages':wages,
            'company_name':company_name,
            'city':city,
            'jobduties':jobduties,
            'company_information':company_information
        }
        self.workdata.append(position)










if __name__ == '__main__':
    spider=Spider()
    workdata=spider.run()
    for i in workdata:
        print(i)