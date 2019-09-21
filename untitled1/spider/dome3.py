#encoding:utf-8
import urllib
from urllib import  request,parse

# url='https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

# resp=request.urlopen(url)
#
# print(resp.read())
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
data = {'first':'true',
    'pn':'1',
    'kd':'python'
}

req=request.Request(url,headers=headers,
date=parse.urlencode(data).encode('utf-8'),method='POST')
resp=request.urlopen(req)

print(resp.read())

