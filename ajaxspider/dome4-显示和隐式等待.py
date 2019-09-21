#encoding=utf-8

from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver_path=r"F:\ruanjian\pythonapp\2.41.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.douban.com/")

#隐式等待必须等待10秒才会查找元素
# driver.implicitly_wait(10)
# driver.find_element_by_id("asdasdasdasd")

#显示等待

element=WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID,'anony-time'))

)
print(element)
