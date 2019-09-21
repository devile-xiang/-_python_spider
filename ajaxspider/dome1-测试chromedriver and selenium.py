#encoding=utf-8

from  selenium import webdriver
import time
from selenium.webdriver.common.by import By


#驱动路径
driver_path=r"F:\ruanjian\pythonapp\2.41.exe"
#把路径配置进去
#
#谷歌版本驱动对照表：https://blog.csdn.net/yoyocat915/article/details/80580066
#谷歌驱动下载表：http://chromedriver.storage.googleapis.com/index.html


driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com/")
#id
# inputTag=driver.find_element_by_id('kw')
#name获取
# inputTag=driver.find_element_by_name('wd')
#class_name获取
# inputTag=driver.find_element_by_class_name('s_ipt')
#xpath获取获取
# inputTag=driver.find_element_by_xpath('//input[@maxlength="255"]')
#js获取
# inputTag=driver.find_element_by_css_selector(".quickdelete-wrap > input")
inputTag=driver.find_element(By.ID,"kw")

inputTag.send_keys('python\n')




time.sleep(5)
driver.quit()
