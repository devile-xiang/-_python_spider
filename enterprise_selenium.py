#encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from lxml import etree
import  time
import re
import xlwt

from selenium.webdriver.common.action_chains import ActionChains





class CO(object):
    driver_path=r"F:\ruanjian\pythonapp\2.41.exe"
    def __init__(self):
        self.driver=webdriver.Chrome(
            #获取goole浏览器启动驱动，在class 下面的derver_path中
            executable_path=CO.driver_path
        )
        self.loginurl="https://www.qixin.com/auth/login"
        self.coinfo=[]
        self.page=7
        self.startpage=6

    def Install_data(self):
        # codatalist=[]
        # for i in range(3):
        #     couser = {
        #         "公司名": "渭南电力有限公司%d"%i,
        #         '公司法人': "为祥和%d"%i,
        #         '公司电话': "1852355561%d"%i,
        #         '公司邮箱': "290463340%d@qq.com"%i,
        #         '公司地址': "渭南市%d"%i,
        #         '公司状态': "开业%d"%i,
        #         '公司资金': "500%d万"%i,
        #         '公司成立日期': "2018年12月1%d"%i,
        #     }
        #     codatalist.append(couser)

        for i,coinfo in enumerate(self.coinfo):
            # print(coinfo)
            newwindow = 'window.open("http://crm.qh0913.com/index.php?m=customer&a=add")'

            # self.driver.get("http://crm.qh0913.com/index.php?m=customer&a=add")

            self.driver.execute_script(newwindow)
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[1])
            # 职位
            position = self.driver.find_element_by_xpath('//input[@name="con_post"]')
            # 手机
            mobile = self.driver.find_element_by_xpath("//input[@name='con_telephone']")
            # 地址
            address = self.driver.find_element_by_xpath("//input[@placeholder='街道信息']")
            # 公司名：
            coname = self.driver.find_element_by_xpath("//input[@id='name']")
            # 联系人：
            contacts_name = self.driver.find_element_by_xpath("//input[@name='con_name']")
            # 邮箱
            email = self.driver.find_element_by_xpath("//input[@name='con_email']")
            # 备注
            description = self.driver.find_element_by_xpath("//textarea[@name='description']")
            # 提交：
            submit = self.driver.find_element_by_xpath("//input[@name='submit']")
            actions = ActionChains(self.driver)
            # driver.switch_to_alert().accept()
            # self.driver.switch_to_alert().accept()
            actions.move_to_element(position)
            actions.send_keys_to_element(position, "法人")
            if len(re.search('\d+', coinfo["公司电话"]).group()) == 11:
                actions.move_to_element(mobile)
                actions.send_keys_to_element(mobile, re.search('\d+', coinfo["公司电话"]).group())
                actions.move_to_element(description)
                actions.send_keys_to_element(description, "公司成立日期：%s-----公司状态：%s-------公司资金:%s" % (
                    coinfo["公司成立日期"], coinfo["公司状态"], coinfo["公司资金"]))
            else:
                # actions.move_to_element(mobile)
                # actions.send_keys_to_element(mobile, "15888888888")
                actions.move_to_element(description)
                actions.send_keys_to_element(description, "%s-----公司成立日期：%s-----公司状态：%s-------公司资金:%s" % (
                    coinfo["公司电话"], coinfo["公司成立日期"], coinfo["公司状态"], coinfo["公司资金"]))
            actions.move_to_element(address)
            actions.send_keys_to_element(address, coinfo["公司地址"])
            actions.move_to_element(coname)
            actions.send_keys_to_element(coname, coinfo["公司名"])
            actions.move_to_element(contacts_name)
            # print(coinfo["公司法人"])
            # print("类型：%s"%coinfo["公司法人"][0])
            user = coinfo["公司法人"]
            user = str(user)
            user = re.sub("法定代表人：", "", user)
            # print(user)
            # print("======================")
            actions.send_keys_to_element(contacts_name, user)
            actions.move_to_element(email)
            actions.send_keys_to_element(email, coinfo["公司邮箱"])
            actions.click(submit)
            actions.perform()
            self.coinfo.pop(i)
            time.sleep(1)
            # alert = self.driver.switch_to.alert
            # alert.accept()
            self.driver.close()







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

        time.sleep(3)


    def run(self):
        self.login()
        self.spiderweinan()
        self.Savedate()
        self.Fantasylogin()
        self.Install_data()
        self.driver.quit()
    def Savedate(self):
        book=xlwt.Workbook(encoding='utf-8',style_compression=0)
        sheet = book.add_sheet('mysheet', cell_overwrite_ok=True)

        for i,data in enumerate(self.coinfo):
            print("公司名字%s"%data['公司名'])
            sheet.write(i, 1, data['公司名'])
            sheet.write(i, 2, data['公司法人'])
            sheet.write(i, 3, data['公司电话'])
            sheet.write(i, 4, data['公司邮箱'])
            sheet.write(i, 5, data['公司地址'])
            sheet.write(i, 6, data['公司状态'])
            sheet.write(i, 7, data['公司资金'])
            sheet.write(i, 8, data['公司成立日期'])

        book.save('codata.xls')




    def spiderweinan(self):
        while True:
            time.sleep(6)
            # break
            if self.startpage >= self.page:
                break;
            else:
                self.driver.get("https://www.qixin.com/search?key=%%E6%%B8%%AD%%E5%%8D%%97&page=%d" % self.startpage)
                sourcr = self.driver.page_source
                self.parse_list_page(sourcr)

                self.startpage=self.startpage + 1

    def parse_list_page(self,sourcr):
        html=etree.HTML(sourcr)

        colists=html.xpath("//div[@class='padding-h-1x border-h-b4 border-t-b4 app-list-items']/div[2]"
                          "/div[@class='col-xs-24 padding-v-1x margin-0-0x border-b-b4 company-item']")



        for i,colist in enumerate(colists):
            # coname = colist.xpath(".//div[@class='company-title']/a/text()")
            # print("公司名称%s" % coname)
            # couser = colist.xpath(".//div[@class='col-2']/div/div[2]/text()")
            # print("公司法人%s" % couser)
            # cotle = colist.xpath(".//div[@class='col-2']/div/div[3]/span[1]/text()")  # extract_first( default="不存在")
            # if len(cotle) <i:
            #     cotle[i]="不存在"
            # print("公司电话%s" % cotle)
            # coemail = colist.xpath(
            #     ".//div[@class='col-2']/div/div[3]/span[2]/a/text()")  # .extract_first( default="不存在")
            # print("公司邮箱：%s" % coemail)
            # if len(coemail) <i:
            #     coemail[i]="不存在"
            # coeaddress = colist.xpath(".//div[@class='col-2']/div/div[4]/span/text()")
            # print("公司地址：%s" % coeaddress)
            # cotype = colist.xpath(".//span[@class='label label-red']/text()")
            # print("公司开业状态：%s" % cotype)
            # com=colist.xpath(".//div[@class='col-3 clearfix font-f2']/div[1]/text()")
            # print("公司的注册资金：%s"%com)
            # startregister=colist.xpath(".//div[@class='col-3-2 text-center content-text']/text()")
            # print("公司成立时间：%s"%startregister)

            coname = colist.xpath(".//div[@class='company-title']/a/text()")
            if len(coname) ==2:
                coname1=coname[0]+"渭南"+coname[1]
            else:
                coname1="渭南"+coname[0]


            # print("公司名称%s" % coname1,end="")
            couser = colist.xpath(".//div[@class='col-2-1']/div[2]/text()")
            # print("公司法人%s" % couser,end="")
            cotle = colist.xpath(".//div[@class='col-2-1']/div[3]/span[1]/text()")
            if len(cotle)<1:
                cotle1="电话为空"
            else:
                cotle1=cotle[0]
            # print("公司电话%s" % cotle1,end="")

            coemail = colist.xpath(".//div[@class='col-2-1']/div[3]/span[2]/a/text()")
            if len(coemail)<1:
                #无邮箱
                coemail1=""
            else:
                coemail1=coemail[0]
            # print("公司邮箱%s" % coemail1,end="")
            coeaddress = colist.xpath(".//div[@class='col-2-1']/div[4]/span/text()")
            # print("公司地址%s" % coeaddress,end="")
            cotype = colist.xpath(".//div[@class='company-tags']/span/text()")
            # print("公司状态%s" % cotype,end="")
            cocapital = colist.xpath(".//div[@class='col-3 clearfix font-f2']/div[1]/text()")
            # print("公司资金%s" % cocapital,end="")
            startregister = colist.xpath(".//div[@class='col-3 clearfix font-f2']/div[2]/text()")
            # print("公司成立日期%s" % startregister)
            # print("="*50)

            codata={
                "公司名":coname1,
                '公司法人':couser[:5],
                '公司电话':cotle1,
                '公司邮箱':coemail1,
                '公司地址':coeaddress[3:],
                '公司状态':cotype,
                '公司资金':cocapital,
                '公司成立日期':startregister
            }
            self.coinfo.append(codata)


    def login(self):
        #这个是登陆代码块
        self.driver.get(self.loginurl)
        #获取手机号码输入框
        name=self.driver.find_element_by_xpath("//input[@placeholder='请输入手机号码']")
        #获取密码输入框
        password=self.driver.find_element_by_xpath("//input[@placeholder='请输入密码']")
        #获取登陆按钮
        submit=self.driver.find_element_by_xpath("//a[@class='btn btn-primary btn-block btn-lg']")

        actions=ActionChains(self.driver)

        actions.move_to_element(name)
        actions.send_keys_to_element(name,"18523555617")
        actions.move_to_element(password)
        actions.send_keys_to_element(password,"1999418xby")
        actions.move_to_element(submit)
        actions.click(submit)
        actions.perform()


        time.sleep(1)



if __name__ == '__main__':
    spider=CO()
    spider.run()

