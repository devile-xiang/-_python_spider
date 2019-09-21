#encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from lxml import etree
import  time
import re
import xlwt
import pymysql
import re
import time
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
        self.page=203
        self.startpage=200

    def Install_data(self):

        # db = pymysql.connect("localhost", "root", "", "crm_qh0913_com")
        db = pymysql.connect('47.104.215.123', 'crm_qh0913_com', 'MHZHEGx5XtrBwnF5', 'crm_qh0913_com',3306)
        # db = pymysql.connect('localhost', 'root', '', 'crm_qh0913_com',3306)
        cursor = db.cursor()

        sqlmax = "select max(customer_id) from jx_customer"
        cursor.execute(sqlmax)
        maxnum = cursor.fetchone()
        # print(maxnum[0])


        for i,data1 in enumerate(self.coinfo):
            # try:
            # i = i + 1 + maxnum[0]

            print("mannum%s"%maxnum)
            print("mannum%s" % len(maxnum))
            if maxnum[0] is None:
                i=1+i
            else:
                i = i + 1 + maxnum[0]


            sql = "select * from jx_customer where name='%s'" % data1['公司名']
            cursor.execute(sql)
            results = cursor.fetchall()
            ticks = time.time()
            ticks = int(ticks)
            if len(results) == 0:


                if  len(data1["公司地址"])>0:
                    address = data1["公司地址"][0]
                    address = str(address)
                    address = re.sub("地址：", "", address)
                    address = re.sub("省", "省\n", address)
                    address = re.sub("市", "市\n", address)
                    address = re.sub("区", "区\n", address)
                else:
                    address="无"

                # print(address)
                sql1 = 'INSERT INTO jx_customer' \
                       '(customer_id,owner_role_id,creator_role_id,' \
                       'contacts_id,name,' \
                       'origin,address,' \
                       'zip_code,industry,' \
                       'annual_revenue,ownership,' \
                       'rating,create_time,' \
                       'update_time,is_deleted,' \
                       'is_locked,delete_time,' \
                       'delete_role_id) values (%d,%d,%d,%d,"%s","","%s","","","","","",%d,0,0,0,0,0)' % \
                       (i, 0, 1, i, data1['公司名'], address, ticks)
                print(sql1)
                cursor.execute(sql1)
                db.commit()


                user = data1["公司法人"][0]
                user = str(user)
                user = re.sub("法定代表人：", "", user)
                # print(data1["公司电话"])
                if data1["公司电话"]=="电话为空":
                    tel = "&nbsp;"

                else:
                    tel = data1["公司电话"]
                    tel = str(tel)
                    tel = re.sub("电话：", "", tel)
                print(tel)
                print(data1['公司邮箱'])
                if data1['公司邮箱']=="":
                    emi = ""
                else:
                    emi = data1['公司邮箱']


                sql2 = 'INSERT into jx_contacts(contacts_id,creator_role_id,name,post,department,sex,saltname,telephone,email,qq_no,address,zip_code,description,create_time,update_time,is_deleted,delete_role_id,delete_time)' \
                       'values (%d,2,"%s","法人","无",0,"未知","%s","%s","","","","","%s","%s",0,0,0)' % (
                       i, user,tel, emi, ticks, ticks)
                print(sql2)
                cursor.execute(sql2)
                db.commit()


                beizhu="公司状态：%s----------公司注册资金：%s----------公司成立日期：%s----------"%(data1['公司状态'][0], data1['公司资金'][0],data1['公司成立日期'][0])
                sql3 = 'INSERT into jx_customer_data(customer_id,description)' \
                       'values (%d,"%s")' % (i,beizhu )
                print(sql3)
                cursor.execute(sql3)
                db.commit()
                print("成功插入数据")
            else:
                print("数据库存在此数据")
                print(results[0][0])
                id = results[0][0]
                id = int(id)
                print(id)
                # "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
                # sql1 = 'INSERT INTO jx_customer' \
                #        '(customer_id,owner_role_id,creator_role_id,' \
                #        'contacts_id,name,' \
                #        'origin,address,' \
                #        'zip_code,industry,' \
                #        'annual_revenue,ownership,' \
                #        'rating,create_time,' \
                #        'update_time,is_deleted,' \
                #        'is_locked,delete_time,' \
                #        'delete_role_id) values (%d,%d,%d,%d,"%s","","%s","","","","","",%d,0,0,0,0,0)' % \
                #        (i, 0, 1, 1, data1['公司名'], data1['公司地址'], ticks)
                # print(sql1)
                # cursor.execute(sql1)
                # db.commit()

                user1 = data1["公司法人"][0]
                user1 = str(user1)
                user1 = re.sub("法定代表人：", "", user1)
                print(user1)
                if data1["公司电话"]=="电话为空":
                    tel1 = "&nbsp;"

                else:
                    tel1 = data1["公司电话"]
                    tel1 = str(tel1)
                    tel1 = re.sub("电话：", "", tel1)
                print(tel1)
                # print(tel1)
                # print(data1['公司邮箱'])
                if data1['公司邮箱']=="":
                    emil = ""
                else:
                    emil = data1['公司邮箱']


                sql4 = 'UPDATE jx_contacts set name="%s" , telephone="%s" , email="%s" , update_time="%s" where contacts_id=%d' \
                       % (user1, tel1,emil, ticks, id)
                print(sql4)
                cursor.execute(sql4)
                db.commit()
                # sql3 = 'INSERT into jx_customer_data(customer_id,description)' \
                #        'values (%d,"%s")' % (
                #        i, data1['公司状态'] + '----------' + data1['公司资金'] + '----------' + data1['公司成立日期'])
                # print(sql3)
                # cursor.execute(sql3)
                # db.commit()
                print("成功更新数据")

            # except Exception:
            #     # print(sql2)
            #     print(Exception)
            #     # print(results)
            #
            #     print("数据库操作出现错误")
            #     db.rollback()
        db.close()






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
        # self.Savedate()
        # self.Fantasylogin()
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
            # print("电话是%s"%cotle1)
            codata={
                "公司名":coname1,
                '公司法人':couser[:5],
                '公司电话':cotle1,
                '公司邮箱':coemail1,
                '公司地址':coeaddress,
                '公司状态':cotype,
                '公司资金':cocapital,
                '公司成立日期':startregister
            }
            self.coinfo.append(codata)


    def login(self):
        #这个是登陆代码块
        self.driver.get(self.loginurl)
        #获取手机号码输入框
        name=self.driver.find_element_by_xpath("//input[@placeholder='请输入11位手机号码']")
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

