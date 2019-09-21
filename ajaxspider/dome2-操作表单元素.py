#endocing:utf-8


from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


#驱动路径
driver_path=r"F:\ruanjian\pythonapp\2.41.exe"
#把路径配置进去
#
#谷歌版本驱动对照表：https://blog.csdn.net/yoyocat915/article/details/80580066
#谷歌驱动下载表：http://chromedriver.storage.googleapis.com/index.html

#操作单选
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get("http://reg.kaixin001.com/")
#
#
# inputTag=driver.find_element_by_id('form_remember')
#
#
#
# time.sleep(2)
# inputTag.click()
# time.sleep(2)
# driver.quit()


#操作select


# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get("http://reg.kaixin001.com/")
#
# selectBth=Select(driver.find_element_by_name('year'))
# time.sleep(2)
# #索引选取
# # selectBth.select_by_index(0)
# #通过内容
# selectBth.select_by_value('1998')
# time.sleep(2)
# driver.quit()

#模拟百度搜索
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com/")

inputTag=driver.find_element_by_id('kw')
inputTag.send_keys('python')
submitTag=driver.find_element_by_id('su')
submitTag.click()
time.sleep(3)
driver.quit()

