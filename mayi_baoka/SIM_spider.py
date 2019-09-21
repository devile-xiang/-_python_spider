#encoding:utf-8


from selenium import webdriver


from selenium.webdriver.common.action_chains import ActionChains
from lxml import etree

import time


class Spider():
    driver_path = r"F:\ruanjian\pythonapp\2.41.exe"
    def __init__(self):
        self.driver=webdriver.Chrome(
            executable_path=Spider.driver_path
        )
        self.url="https://m.10010.com/queen/alibao/fill.html?product=1"
    def main(self):








        # action=






        while True:

            self.driver.get(self.url)
            time.sleep(10)
            sourcr = self.driver.page_source
            # print(sourcr)
            html=etree.HTML(sourcr)
            # number_ul=html.xpath("//ul[@class='number-list']")

            li_list=html.xpath("//a/text()")
            print(li_list)
            time.sleep(8)












if __name__ == '__main__':
    Spider=Spider()
    Spider.main()