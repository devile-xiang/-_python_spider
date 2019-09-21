#encoding:utf-8


import requests

#设置代理
proxy={
    'http': '122.230.52.253:16267'
}
requests=requests.get("http://httpbin.org/ip",proxies=proxy)
print(requests.text)