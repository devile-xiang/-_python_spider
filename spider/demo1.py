
#encoding:utf-8
from urllib import request
from urllib import  parse


# urlretrieve的用法
# request.urlretrieve('http://www.baidu.com/','baidu.html')


#urlencode函数的用法
# parame={'name':'张三','age':18 ,'greet':'hello,world'}
# result=parse.urlencode(parame)
# print(result)

# url='http://www.baidu.com/s'
# params={"wd":"刘德华"}
# qs=parse.urlencode(params)
# url=url+"?"+qs
# print(url)
# resp=request.urlopen(url)
# print(resp.read())

#parse_qs函数用法
parame={'name':'张三','age':18 ,'greet':'hello,world'}
qs=parse.urlencode(parame)
print(qs)
result=parse.parse_qs(qs)
print(result)