#encoding=utf-8

from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
import time

driver_path=r"F:\ruanjian\pythonapp\2.41.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com/")


for cookie in driver.get_cookies():
    print(cookie)
print('='*30)
print(driver.get_cookie("PSTM"))
print('='*30)
driver.delete_cookie("PSTM")
print(driver.get_cookie("PSTM"))

driver.delete_all_cookies()
