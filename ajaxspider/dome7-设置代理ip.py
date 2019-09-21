#encoding:utf-8

from selenium import webdriver



driver_path = r"F:\ruanjian\pythonapp\2.41.exe"
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://114.235.152.23:8060")

driver = webdriver.Chrome(executable_path=driver_path , chrome_options=options)

driver.get("http://httpbin.org/ip")

