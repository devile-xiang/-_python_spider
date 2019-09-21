#encoding:utf-8
import time
from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.action_chains import ActionChains
import re
import xlwt

class Ylspider(object):
    driver_path = r"F:\ruanjian\pythonapp\2.41.exe"
    def __init__(self):
        self.data=[]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=zh_CN.UTF-8')
        options.add_argument(
            'User-Agent="Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36"')

        self.driver = webdriver.Chrome(executable_path=Ylspider.driver_path,chrome_options=options)
        self.url="http://iesayoung.com/crm/crm/customer"
        self.page=357
        self.startpage=0

    def run(self):
        self.login()
        self.driver.get(self.url)
        while True:
            self.startpage=self.startpage+1

            sourcr=self.driver.page_source
            userdata=self.parse_list_page(sourcr)
            for i in userdata:
                self.data.append(i)
            # 下来滚动条到最底部
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)");
            time.sleep(5)



            next_bth =self.driver.find_element_by_xpath('//div[@class="pagination"]/ul/li[last()-1]/a')
            # print("当前是%d页"%self.page)
            if self.startpage >=self.page:
                break
            else:
                # self.driver.execute_script("$(arguments[0]).click()",next_bth)
                next_bth.click()
                # time.sleep(1)
                # next_bth.click()


        return self.data



    def parse_list_page(self,sourcr):
        html=etree.HTML(sourcr)
        userinfo=html.xpath("//tbody/tr/td[3]/text()")
        phoneinfo=html.xpath("//tbody/tr/td[5]/text()")
        textinfo=html.xpath("//tbody/tr/td[6]/text()")

        userinfodata=[]
        # print(len(textinfo))
        # print(len(userinfo))
        for i in range(0,len(textinfo)):
            a={


                "个人信息":userinfo[i*4].strip()+"-"*5+userinfo[(i*4)+1].strip()+"-"*5+userinfo[(i*4)+2].strip()+"-"*5+userinfo[(i*4)+3].strip(),
                "联系方式":phoneinfo[i*4].strip()+"-"*5+userinfo[(i*4)+1].strip()+"-"*5+userinfo[(i*4)+2].strip()+"-"*5+userinfo[(i*4)+3].strip(),
                "备注信息":textinfo[i].strip()

            }
            userinfodata.append(a)
            # print("个人信息")
            # print(a["个人信息"])
        print("="*10+"用户合集"+"="*10)
        print(userinfodata)
        return userinfodata




    def login(self):

        self.driver.get("http://iesayoung.com/crm/login")

        name = self.driver.find_element_by_xpath('//input[@placeholder="请输入登录账号"]')
        password = self.driver.find_element_by_xpath('//input[@placeholder="请输入密码"]')

        submit = self.driver.find_element_by_xpath('//input[@lay-filter="formSubmit"]')

        actions = ActionChains(self.driver)
        # 选择这个输入框
        actions.move_to_element(name)
        # 在输入框中写入数据
        actions.send_keys_to_element(name, 'lixiangqian')
        actions.move_to_element(password)
        actions.send_keys_to_element(password, '95992959')
        actions.move_to_element(submit)
        actions.click(submit)
        #
        actions.perform()

if __name__ == '__main__':
    spider=Ylspider()
    data=spider.run()

    book=xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet=book.add_sheet("mysheet",cell_overwrite_ok=True)
    for i,k in enumerate(data):
        print("i：%s，K:%s"%(i,k))
        print("="*30)
        print(k["个人信息"].strip())
        sheet.write(i ,1,k["个人信息"].strip())
        sheet.write(i ,2,k["联系方式"].strip())
        sheet.write(i, 3,k["备注信息"].strip())
        print(k)
    book.save('医疗数据.xls')



