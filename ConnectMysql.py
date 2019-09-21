#encoding:utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import time

class Istall(object):
    driver_path = r"F:\ruanjian\pythonapp\2.41.exe"
    def __init__(self):
        self.driver = webdriver.Chrome(
            # 获取goole浏览器启动驱动，在class 下面的derver_path中
            executable_path=Istall.driver_path
        )
        self.loginurl = "https://www.qixin.com/auth/login"
    def run(self):
        self.Fantasylogin()
        self.Install_data()
    def Install_data(self):
        codatalist=[]
        for i in range(3):
            couser = {
                "公司名": "渭南电力有限公司%d"%i,
                '公司法人': "为祥和%d"%i,
                '公司电话': "1852355561%d"%i,
                '公司邮箱': "290463340%d@qq.com"%i,
                '公司地址': "渭南市%d"%i,
                '公司状态': "开业%d"%i,
                '公司资金': "500%d万"%i,
                '公司成立日期': "2018年12月1%d"%i,
            }
            codatalist.append(couser)

        for i,coinfo in enumerate(codatalist):
            self.driver.get("http://crm.qh0913.com/index.php?m=leads&a=add")
            #职位
            position=self.driver.find_element_by_xpath("//input[@id='position']")
            #手机
            mobile=self.driver.find_element_by_xpath("//input[@id='mobile']")
            #地址
            address=self.driver.find_element_by_xpath("//input[@placeholder='街道信息']")
            #公司名：
            coname=self.driver.find_element_by_xpath("//input[@id='name']")
            #联系人：
            contacts_name=self.driver.find_element_by_xpath("//input[@id='contacts_name']")
            #邮箱
            email=self.driver.find_element_by_xpath("//input[@id='email']")
            #备注
            description=self.driver.find_element_by_xpath("//textarea[@id='description']")
            #提交：
            submit=self.driver.find_element_by_xpath("//input[@name='submit']")

            actions=ActionChains(self.driver)

            actions.move_to_element(position)
            actions.send_keys_to_element(position,"法人")
            actions.move_to_element(mobile)
            actions.send_keys_to_element(mobile,coinfo["公司电话"])
            actions.move_to_element(address)
            actions.send_keys_to_element(address,coinfo["公司地址"])
            actions.move_to_element(coname)
            actions.send_keys_to_element(coname,coinfo["公司名"])
            actions.move_to_element(contacts_name)
            actions.send_keys_to_element(contacts_name,coinfo["公司法人"])
            actions.move_to_element(email)
            actions.send_keys_to_element(email,coinfo["公司邮箱"])
            actions.move_to_element(description)
            actions.send_keys_to_element(description,"公司成立日期："+coinfo["公司成立日期"]+"/n公司状态："+coinfo["公司状态"]+"/n公司资金:"+coinfo["公司资金"])
            actions.click(submit)
            actions.perform()






    def Fantasylogin(self):
        self.driver.get('http://crm.qh0913.com/index.php?m=user&a=login')
        name=self.driver.find_element_by_xpath("//input[@name='name']")
        password=self.driver.find_element_by_xpath("//input[@name='password']")
        submit=self.driver.find_element_by_xpath("//input[@name='submit']")

        actions=ActionChains(self.driver)
        actions.move_to_element(name)
        actions.send_keys_to_element(name,"admin888")
        actions.move_to_element(password)
        actions.send_keys_to_element(password,"123456")
        actions.click(submit)
        actions.perform()

        time.sleep(1)







if __name__ == '__main__':
    spider=Istall()
    spider.run()