#encoding:UTF-8

from urllib import request,parse
from http.cookiejar import  CookieJar

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }
#1.登陆
# 创建一个COOKiejar对象
def get_opener():

    cookiejar=CookieJar()

    handler=request.HTTPCookieProcessor(cookiejar)

    opener=request.build_opener(handler)
    return opener

def login_renren(opener):

    data={
        'email':'18523555617',
        'password':'1999418xby'
    }
    login_url="http://www.renren.com/PLogin.do"
    req=request.Request(login_url,data=parse.urlencode(data).encode('utf-8'),headers=headers)
    opener.open(req)


#访问个人主页
def visit_profile(opener):
    dapeng_url="http://www.renren.com/880151247/profile"
    #获取个人主页2信息的时候，不要新建一个opener,应该是用以前的opener,因为之前的opener的
    # 包含了cookiek
    req=request.Request(dapeng_url,headers=headers)
    resp=opener.open(req)
    with open('renren.html','w',encoding='utf-8') as fp:
            fp.write(resp.read().decode('utf-8'))
if __name__ == '__main__':
    opener=get_opener()
    login_renren(opener)
    visit_profile(opener)