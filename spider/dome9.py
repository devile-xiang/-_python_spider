#encoding:utf-8
import requests
# requests=requests.get("https://www.baidu.com")
# # #字典显示.get_dict()
# # print(requests.cookies.get_dict())
# #
# # print(requests)


session=requests.session()
login_url="http://www.renren.com/PLogin.do"
data = {'email': '18523555617','password': '1999418xby'}
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36" }

session.post(login_url,data=data,headers=headers)

response=session.get("http://www.renren.com/880151247/profile")

with open('dapeng.html','w',encoding='utf-8') as pf:
    pf.write(response.text)