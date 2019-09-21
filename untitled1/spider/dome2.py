#encoding:utf-8

from urllib import  parse

url ='https://www.baidu,com/s?wd=python&username=abc#1'
# result=parse.urlparse(url)
result=parse.urlsplit(url)
print('sheme:',result.scheme)
print('netloc:',result.netloc)
print('path:',result.path)
# print('params:',result.params)
print('query:',result.query)
print('fragment:',result.fragment)