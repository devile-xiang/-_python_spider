#encoding:utf-8



from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
class Qiangpiao(object):
    def __init__(self):
        self.login_url="https://kyfw.12306.cn/otn/resources/login.html"
        self.initmy_url="https://kyfw.12306.cn/otn/view/index.html"
        self.search_url="https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"
        self.driver=webdriver.Chrome(
            executable_path=r"F:\ruanjian\pythonapp\2.41.exe"
        )
    def wait_input(self):
        self.from_station=input("起始站：")
        self.to_station=input("目的地：")
        self.depart_time=input("出发时间：")
        self.passengers=input("乘客姓名（如果有多个乘客，用英文丢好隔开）").split(",")
        self.trains=input("车次（如有多个车次用英文逗号隔开）").split(",")

    def _login(self):
        self.driver.get(self.login_url)
        #显示等待

        #隐式等待
        WebDriverWait(self.driver,1000).until(EC.url_to_be(self.initmy_url))
        print("登陆成功")

    def _order_ticket(self):
        #跳转到查余票
        self.driver.get(self.search_url)
        #2.等待用户输入出发地是否输入正确
        WebDriverWait(self.driver,1000).until(
            EC.text_to_be_present_in_element_value

        )
        #目的地
        WebDriverWait(self.driver,1000).until(
            EC.text_to_be_present_in_element_value((By.ID,"toStationText"),self.to_station)
        )
        #出发时间
        WebDriverWait(self.driver,1000).until((EC.text_to_be_present_in_element_value((By.ID,"train_date"),self.depart_time)                                       ))
        #等待查询按钮是否可用
        WebDriverWait(self.driver,1000).until(
            EC.element_to_be_clickable((By.ID,"query_ticket"))
        )
        #如果能够被点击，name就找到这个查询按钮，执行点击事件

        searchBth=self.driver.find_element_by_id("query_ticket")
        searchBth.click()


    def run(self):
        self.wait_input()
        self._login()
        self._order_ticket()

if __name__ == '__main__':
    spider = Qiangpiao()
    spider.run()