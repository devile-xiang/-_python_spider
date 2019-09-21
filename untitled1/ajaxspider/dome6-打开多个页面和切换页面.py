#encoding:utf-8

from selenium import webdriver

driver_path=r"F:\ruanjian\pythonapp\2.41.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.douban.com/")

#用js开大新的页面
driver.execute_script("window.open('https://baidu.com/')")

print(driver.current_url)
#切换到指定的窗口第一个下标为0，第二个为1
driver.switch_to.window(driver.window_handles[1])
#显示代码现在使用的driver的页面网址
print(driver.current_url)