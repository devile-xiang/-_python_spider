from selenium import webdriver

from lxml import etree


def main():
    driver_path = r"F:\ruanjian\pythonapp\2.41.exe"
    driver = webdriver.Chrome(
        executable_path=driver_path
    )
    driver.get("http://www.baidu.com")
    html=driver.page_source
    print(html)
if __name__ == '__main__':
    main()
