#encoding：utf-8


from selenium import webdriver
from lxml import etree
import time
import re
import csv
from selenium.webdriver.chrome.options import Options



#导入操作连
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
class Spider(object):
    driver_path = r"F:\ruanjian\pythonapp\2.41.exe"
    def __init__(self):
        # chrome_options=Options()
        # chrome_options.add_argument('--headless')


        self.driver = webdriver.Chrome(
            executable_path=Spider.driver_path
        )
        # self.driver=webdriver.Chrome(chrome_options=chrome_options)
        self.page_url="http://www.023sogou.com/adminjiuybjki/not_order.asp?keyword=&btime=&etime=&pay=&zt=&kuaidi=&cname=&gzid=&page=4"
        self.login_url="http://www.023sogou.com/adminjiuybjki/login.asp"
        self.username="admin"
        self.userpwd="YU4hjk&4M"
        self.page_num_url="http://www.023sogou.com/adminjiuybjki/not_duopin.asp?keyword=&page=1"
        self.data=[]
    def run(self):
        self.login_user()
        self.driver.get(self.page_num_url)
        source=self.driver.page_source
        page_max=self.page_num(source)

        print("解析第一页，返回的总页数是：%s"%page_max)
        page_max=int(page_max)
        for i in range(0,42):
            page_url="http://www.023sogou.com/adminjiuybjki/not_order.asp?keyword=&btime=&etime=&pay=&zt=&kuaidi=&cname=&gzid=&page=%s"% i
            time.sleep(2)
            self.Obtain_page(page_url)
        # for i,x in enumerate(self.data):
        #     print("第%d行数据为:商品：%s-------个人信息：%s---------收货地址：%s"%(i,x["commodity"],x["userinfo"],x["address"]))
        # print(self.data)
        headers=['商品','个人信息','收货地址']
        with open('data.csv','w',encoding='utf-8',newline='') as fp:
            writer =csv.writer(fp)
            writer.writerow(headers)
            for i in self.data:
                writer.writerow(i)


    def Obtain_page(self,page_url):
        #数据爬取
        open_url="window.open('%s')"%page_url
        print(open_url)

        self.driver.execute_script(open_url)
        self.driver.switch_to.window(self.driver.window_handles[1])

        #获取当前页面的源代码
        html = self.driver.page_source
        html=etree.HTML(html)
        commodity=html.xpath('//tbody/tr[not(@class="color1")]/td[3]/div[1]/text()')
        # print("商品：%s"%commodity)
        userinfo = html.xpath('//tbody/tr[not(@class="color1")]/td[4]/text()')
        print(type(userinfo))


        userinfo1=[]

        for i in range(0,len(userinfo)):
            if len(userinfo[i]) >4 :
                print(userinfo[i])
                userinfo1.append(userinfo[i])

        #收货地址
        address=html.xpath('//tbody/tr/td[4]/div[1]/text()')
        # print("收货地址：%s"%address)


        for i in range(0,len(commodity)):

            # print("商品：%s,收货信息：%s,收货地址是：%s" %(commodity[i],userinfo[i],address[i]))
            userdata=[commodity[i],userinfo1[i].strip(),address[i],]
            self.data.append(userdata)

        # address = html.xpath("//div/text()")
        # print("地址：" % address)
        # address1 = html.xpath("//tbody/tr/td[6]/div/text()")
        # print("IP地址：%s" % address1)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def page_num(self,source):
        html=etree.HTML(source)
        page_max=html.xpath('//div[@class="pagination"]/a[last()]/@href')
        ret=re.search('\d{2}',page_max[0])
        return ret.group()




    def login_user(self):
        self.driver.get(self.login_url)
        name=self.driver.find_element_by_id("username")
        password=self.driver.find_element_by_id("password")
        submit=self.driver.find_element_by_id("btnPost")
        #准备开始操作链
        actions=ActionChains(self.driver)
        #选择用户名输入框
        actions.move_to_element(name)
        #输入用户名
        actions.send_keys_to_element(name,self.username)
        #选择用户密码输入框
        actions.move_to_element(password)
        #输入用户密码
        actions.send_keys_to_element(password,self.userpwd)
        actions.click(submit)
        actions.perform()





if __name__ == '__main__':
    Spider=Spider()
    Spider.run()