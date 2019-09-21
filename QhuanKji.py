from selenium import webdriver #line:2
from lxml import etree #line:3
import time #line:4
import re #line:5
import xlwt #line:6
from selenium .webdriver .common .action_chains import ActionChains #line:8
class CO (object ):#line:14
    driver_path =r"F:\ruanjian\pythonapp\2.41.exe"#line:15
    def __init__ (O00OO0O00O00O000O ):#line:16
        O00OO0O00O00O000O .driver =webdriver .Chrome (executable_path =CO .driver_path )#line:20
        O00OO0O00O00O000O .loginurl ="https://www.qixin.com/auth/login"#line:21
        O00OO0O00O00O000O .coinfo =[]#line:22
        O00OO0O00O00O000O .page =6 #line:23
        O00OO0O00O00O000O .startpage =0 #line:24
    def Install_data (OOOOOOOOOOOOOOO0O ):#line:26
        for O0000OO00O00O00OO ,OOO0OO000OOOO00OO in enumerate (OOOOOOOOOOOOOOO0O .coinfo ):#line:41
            OOOOOOOOOOOOOOO0O .driver .get ("http://crm.qh0913.com/index.php?m=leads&a=add")#line:46
            OOO0OOO00OO00O0O0 =OOOOOOOOOOOOOOO0O .driver .find_element_by_xpath ("//input[@id='position']")#line:48
            O000OO00OOOO0000O =OOOOOOOOOOOOOOO0O .driver .find_element_by_xpath ("//input[@id='mobile']")#line:50
            O0OO0OO0O000O0OO0 =OOOOOOOOOOOOOOO0O .driver .find_element_by_xpath ("//input[@placeholder='街道信息']")#line:52
            OOO00OO0O00OO00OO =OOOOOOOOOOOOOOO0O .driver .find_element_by_xpath ("//input[@id='name']")#line:54
            OOOO0OO00OOO0OOOO =OOOOOOOOOOOOOOO0O .driver .find_element_by_xpath ("//input[@id='contacts_name']")#line:56
            OOO0OO0OO00OOO000 =OOOOOOOOOOOOOOO0O .driver .find_element_by_xpath ("//input[@name='email']")#line:58
            O0OO000000OO0OO0O =OOOOOOOOOOOOOOO0O .driver .find_element_by_xpath ("//textarea[@id='description']")#line:60
            O000O0000OOOO0OOO =OOOOOOOOOOOOOOO0O .driver .find_element_by_xpath ("//input[@name='submit']")#line:62
            OOOOOOO00O0000OO0 =ActionChains (OOOOOOOOOOOOOOO0O .driver )#line:64
            OOOOOOO00O0000OO0 .move_to_element (OOO0OOO00OO00O0O0 )#line:67
            OOOOOOO00O0000OO0 .send_keys_to_element (OOO0OOO00OO00O0O0 ,"法人")#line:68
            if len (re .search ('\d+',OOO0OO000OOOO00OO ["公司电话"]).group ())==11 :#line:70
                OOOOOOO00O0000OO0 .move_to_element (O000OO00OOOO0000O )#line:71
                OOOOOOO00O0000OO0 .send_keys_to_element (O000OO00OOOO0000O ,re .search ('\d+',OOO0OO000OOOO00OO ["公司电话"]).group ())#line:72
                OOOOOOO00O0000OO0 .move_to_element (O0OO000000OO0OO0O )#line:73
                OOOOOOO00O0000OO0 .send_keys_to_element (O0OO000000OO0OO0O ,"公司成立日期：%s-----公司状态：%s-------公司资金:%s"%(OOO0OO000OOOO00OO ["公司成立日期"],OOO0OO000OOOO00OO ["公司状态"],OOO0OO000OOOO00OO ["公司资金"]))#line:75
            else :#line:76
                OOOOOOO00O0000OO0 .move_to_element (O000OO00OOOO0000O )#line:77
                OOOOOOO00O0000OO0 .send_keys_to_element (O000OO00OOOO0000O ,"15888888888")#line:78
                OOOOOOO00O0000OO0 .move_to_element (O0OO000000OO0OO0O )#line:79
                OOOOOOO00O0000OO0 .send_keys_to_element (O0OO000000OO0OO0O ,"%s-----公司成立日期：%s-----公司状态：%s-------公司资金:%s"%(OOO0OO000OOOO00OO ["公司电话"],OOO0OO000OOOO00OO ["公司成立日期"],OOO0OO000OOOO00OO ["公司状态"],OOO0OO000OOOO00OO ["公司资金"]))#line:81
            OOOOOOO00O0000OO0 .move_to_element (O0OO0OO0O000O0OO0 )#line:83
            OOOOOOO00O0000OO0 .send_keys_to_element (O0OO0OO0O000O0OO0 ,OOO0OO000OOOO00OO ["公司地址"])#line:84
            OOOOOOO00O0000OO0 .move_to_element (OOO00OO0O00OO00OO )#line:85
            OOOOOOO00O0000OO0 .send_keys_to_element (OOO00OO0O00OO00OO ,OOO0OO000OOOO00OO ["公司名"])#line:86
            OOOOOOO00O0000OO0 .move_to_element (OOOO0OO00OOO0OOOO )#line:87
            OOOOOOO00O0000OO0 .send_keys_to_element (OOOO0OO00OOO0OOOO ,OOO0OO000OOOO00OO ["公司法人"])#line:88
            OOOOOOO00O0000OO0 .move_to_element (OOO0OO0OO00OOO000 )#line:89
            OOOOOOO00O0000OO0 .send_keys_to_element (OOO0OO0OO00OOO000 ,OOO0OO000OOOO00OO ["公司邮箱"])#line:90
            OOOOOOO00O0000OO0 .click (O000O0000OOOO0OOO )#line:92
            OOOOOOO00O0000OO0 .perform ()#line:93
    def Fantasylogin (O00OOOO0OO0OO00O0 ):#line:100
        O00OOOO0OO0OO00O0 .driver .get ('http://crm.qh0913.com/index.php?m=user&a=login')#line:101
        O0O0OO00O00OO0OOO =O00OOOO0OO0OO00O0 .driver .find_element_by_xpath ("//input[@name='name']")#line:102
        OO000OO0O0O000OOO =O00OOOO0OO0OO00O0 .driver .find_element_by_xpath ("//input[@name='password']")#line:103
        OOOOO00OOOO0OO000 =O00OOOO0OO0OO00O0 .driver .find_element_by_xpath ("//input[@name='submit']")#line:104
        O0000O0O00O000O00 =ActionChains (O00OOOO0OO0OO00O0 .driver )#line:106
        O0000O0O00O000O00 .move_to_element (O0O0OO00O00OO0OOO )#line:107
        O0000O0O00O000O00 .send_keys_to_element (O0O0OO00O00OO0OOO ,"admin888")#line:108
        O0000O0O00O000O00 .move_to_element (OO000OO0O0O000OOO )#line:109
        O0000O0O00O000O00 .send_keys_to_element (OO000OO0O0O000OOO ,"123456")#line:110
        O0000O0O00O000O00 .click (OOOOO00OOOO0OO000 )#line:111
        O0000O0O00O000O00 .perform ()#line:112
        time .sleep (1 )#line:114
    def run (O0000OO0O0OO00OOO ):#line:117
        O0000OO0O0OO00OOO .login ()#line:118
        O0000OO0O0OO00OOO .spiderweinan ()#line:119
        O0000OO0O0OO00OOO .Savedate ()#line:120
        O0000OO0O0OO00OOO .Fantasylogin ()#line:121
        O0000OO0O0OO00OOO .Install_data ()#line:122
    def Savedate (O00O0OOO0O0O00OOO ):#line:123
        OOO0OOOOOO0000O0O =xlwt .Workbook (encoding ='utf-8',style_compression =0 )#line:124
        O0OOOOO0O0000O000 =OOO0OOOOOO0000O0O .add_sheet ('mysheet',cell_overwrite_ok =True )#line:125
        for OOO0OOO0OOOO00OOO ,OOO00O0OOO0000OO0 in enumerate (O00O0OOO0O0O00OOO .coinfo ):#line:127
            print ("公司名字%s"%OOO00O0OOO0000OO0 ['公司名'])#line:128
            O0OOOOO0O0000O000 .write (OOO0OOO0OOOO00OOO ,1 ,OOO00O0OOO0000OO0 ['公司名'])#line:129
            O0OOOOO0O0000O000 .write (OOO0OOO0OOOO00OOO ,2 ,OOO00O0OOO0000OO0 ['公司法人'])#line:130
            O0OOOOO0O0000O000 .write (OOO0OOO0OOOO00OOO ,3 ,OOO00O0OOO0000OO0 ['公司电话'])#line:131
            O0OOOOO0O0000O000 .write (OOO0OOO0OOOO00OOO ,4 ,OOO00O0OOO0000OO0 ['公司邮箱'])#line:132
            O0OOOOO0O0000O000 .write (OOO0OOO0OOOO00OOO ,5 ,OOO00O0OOO0000OO0 ['公司地址'])#line:133
            O0OOOOO0O0000O000 .write (OOO0OOO0OOOO00OOO ,6 ,OOO00O0OOO0000OO0 ['公司状态'])#line:134
            O0OOOOO0O0000O000 .write (OOO0OOO0OOOO00OOO ,7 ,OOO00O0OOO0000OO0 ['公司资金'])#line:135
            O0OOOOO0O0000O000 .write (OOO0OOO0OOOO00OOO ,8 ,OOO00O0OOO0000OO0 ['公司成立日期'])#line:136
        OOO0OOOOOO0000O0O .save ('codata.xls')#line:138
    def spiderweinan (OOOOO0OO00OOO00OO ):#line:143
        while True :#line:144
            time .sleep (6 )#line:145
            if OOOOO0OO00OOO00OO .startpage >=OOOOO0OO00OOO00OO .page :#line:147
                break ;#line:148
            else :#line:149
                OOOOO0OO00OOO00OO .driver .get ("https://www.qixin.com/search?key=%%E6%%B8%%AD%%E5%%8D%%97&page=%d"%OOOOO0OO00OOO00OO .startpage )#line:150
                O0O00O0O0OO0000OO =OOOOO0OO00OOO00OO .driver .page_source #line:151
                OOOOO0OO00OOO00OO .parse_list_page (O0O00O0O0OO0000OO )#line:152
                OOOOO0OO00OOO00OO .startpage =OOOOO0OO00OOO00OO .startpage +1 #line:154
    def parse_list_page (OOOOOO00OO0OOOO00 ,O0OO0000O0000OOOO ):#line:156
        OO0OOO00OOOOO0O0O =etree .HTML (O0OO0000O0000OOOO )#line:157
        OOOOOOO00000OO000 =OO0OOO00OOOOO0O0O .xpath ("//div[@class='padding-h-1x border-h-b4 border-t-b4 app-list-items']/div[2]" "/div[@class='col-xs-24 padding-v-1x margin-0-0x border-b-b4 company-item']")#line:160
        for OO00OO000OOO0OO00 ,OO000OOOOO0OO00OO in enumerate (OOOOOOO00000OO000 ):#line:164
            O0O0O00OOO00O0O00 =OO000OOOOO0OO00OO .xpath (".//div[@class='company-title']/a/text()")#line:187
            if len (O0O0O00OOO00O0O00 )==2 :#line:188
                OOOO0OOO0O0O0O0OO =O0O0O00OOO00O0O00 [0 ]+"渭南"+O0O0O00OOO00O0O00 [1 ]#line:189
            else :#line:190
                OOOO0OOO0O0O0O0OO ="渭南"+O0O0O00OOO00O0O00 [0 ]#line:191
            OOO0OOO0O00O0OOOO =OO000OOOOO0OO00OO .xpath (".//div[@class='col-2-1']/div[2]/text()")#line:195
            OO000O0OOOOOOO000 =OO000OOOOO0OO00OO .xpath (".//div[@class='col-2-1']/div[3]/span[1]/text()")#line:197
            if len (OO000O0OOOOOOO000 )<1 :#line:198
                OOO0O00O0OOO00O0O ="电话为空"#line:199
            else :#line:200
                OOO0O00O0OOO00O0O =OO000O0OOOOOOO000 [0 ]#line:201
            OOO00000OO00O0OOO =OO000OOOOO0OO00OO .xpath (".//div[@class='col-2-1']/div[3]/span[2]/a/text()")#line:204
            if len (OOO00000OO00O0OOO )<1 :#line:205
                O00OOOOO00O0OOOO0 =""#line:207
            else :#line:208
                O00OOOOO00O0OOOO0 =OOO00000OO00O0OOO [0 ]#line:209
            O0OO0O000000O00OO =OO000OOOOO0OO00OO .xpath (".//div[@class='col-2-1']/div[4]/span/text()")#line:211
            OOOOO00OO0O0OOOO0 =OO000OOOOO0OO00OO .xpath (".//div[@class='company-tags']/span/text()")#line:213
            OOO0O00O000OOO0O0 =OO000OOOOO0OO00OO .xpath (".//div[@class='col-3 clearfix font-f2']/div[1]/text()")#line:215
            O0O000O0000O0O0OO =OO000OOOOO0OO00OO .xpath (".//div[@class='col-3 clearfix font-f2']/div[2]/text()")#line:217
            OO0OOO0O000O0O0OO ={"公司名":OOOO0OOO0O0O0O0OO ,'公司法人':OOO0OOO0O00O0OOOO ,'公司电话':OOO0O00O0OOO00O0O ,'公司邮箱':O00OOOOO00O0OOOO0 ,'公司地址':O0OO0O000000O00OO ,'公司状态':OOOOO00OO0O0OOOO0 ,'公司资金':OOO0O00O000OOO0O0 ,'公司成立日期':O0O000O0000O0O0OO }#line:230
            OOOOOO00OO0OOOO00 .coinfo .append (OO0OOO0O000O0O0OO )#line:231
    def login (O000000OOO0O0OO00 ):#line:234
        O000000OOO0O0OO00 .driver .get (O000000OOO0O0OO00 .loginurl )#line:236
        O0O00OO000O00OOOO =O000000OOO0O0OO00 .driver .find_element_by_xpath ("//input[@placeholder='请输入手机号码']")#line:238
        O000O00O0O0OO00O0 =O000000OOO0O0OO00 .driver .find_element_by_xpath ("//input[@placeholder='请输入密码']")#line:240
        OOO000O00OOOO0O00 =O000000OOO0O0OO00 .driver .find_element_by_xpath ("//a[@class='btn btn-primary btn-block btn-lg']")#line:242
        O00OOOO0OO0OOOOO0 =ActionChains (O000000OOO0O0OO00 .driver )#line:244
        O00OOOO0OO0OOOOO0 .move_to_element (O0O00OO000O00OOOO )#line:246
        O00OOOO0OO0OOOOO0 .send_keys_to_element (O0O00OO000O00OOOO ,"18523555617")#line:247
        O00OOOO0OO0OOOOO0 .move_to_element (O000O00O0O0OO00O0 )#line:248
        O00OOOO0OO0OOOOO0 .send_keys_to_element (O000O00O0O0OO00O0 ,"1999418xby")#line:249
        O00OOOO0OO0OOOOO0 .move_to_element (OOO000O00OOOO0O00 )#line:250
        O00OOOO0OO0OOOOO0 .click (OOO000O00OOOO0O00 )#line:251
        O00OOOO0OO0OOOOO0 .perform ()#line:252
        time .sleep (1 )#line:255
if __name__ =='__main__':#line:259
    spider =CO ()#line:260
    spider .run ()#line:261
