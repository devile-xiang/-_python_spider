#encoding:UTF-8

from  urllib import request
from http.cookiejar import MozillaCookieJar

cookiejar=MozillaCookieJar('cookie.txt')
cookiejar.load()
#加载cookie已过期的cookie,要在load()里放ignore_discard=True
handler=request.HTTPCookieProcessor(cookiejar)
opener=request.build_opener(handler)

resp=opener.open('http://httpbin.org/cookies/set?name=xiang')
for cookie in cookiejar:
    print(cookie)
# cookiejar.save(ignore_discard=True)