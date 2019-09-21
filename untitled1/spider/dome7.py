# encoding:utf-8


import requests

# requests=requests.get("https://www.baidu.com/")
# print(type(requests.text))
# print(requests.text.encode("utf-8"))
# print(type(requests.content))
# print(requests.content.decode('UTF-8'))

#
# print(requests.url)#网址
# print(requests.encoding)#编码类型
# print(requests.status_code)#返回参数


params={
    'wd':'中国'
}

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}



requests=requests.get("https://www.baidu.com/s",params=params,headers=headers)

with open('baidu.html','w',encoding='utf-8')as fp:
    fp.write(requests.content.decode('utf-8'))
print(requests.url)
