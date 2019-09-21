#encoding:utf-8


from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


driver_path=r"F:\ruanjian\pythonapp\2.41.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com/")

submitBth=driver.find_element_by_id('su')
print(type(submitBth))

print(submitBth.get_attribute("value"))
#截图页面必须到刀driver
driver.save_screenshot("baidu.png")
