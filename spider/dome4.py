#encoding:utf-8

#http://www.renren.com/880151247/profile
#登陆网址：http://www.renren.com/SysHome.do



#不适用cookie去请求用户页面
from urllib import request


dapeng_url="http://www.renren.com/880151247/profile"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Cookie":"anonymid=jk9dcgwm-2acxxg; depovince=GW; _r01_=1; JSESSIONID=abcujFTyKNnUadZfDmVtw; ick_login=b6acc9fd-6563-42f8-bda9-"
             "9639f239050b; ick=78fd3f79-17d7-4bb5-a5e9-45da0b81a0fc; __utma=151146938.2014790755.1533021472.1533021472.1533021472.1; "
             "__utmc=151146938; __utmz=151146938.1533021472.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; first_lo"
             "gin_flag=1; ln_uact=18523555617; ln_hurl=http://hdn.xnimg.cn/photos/hdn321/20180510/1215/h_main_0Jsy_53900008e6561986.jpg; wp_"
             "fold=0; XNESSESSIONID=13efd00a3c96; jebecookies=96c0b032-4a0e-469f-a460-76c06128bde2|||||; _de=006BDB15A7E3477686B671BB0A41F7A6;"
             " p=b7469728f01411aaa533aab3561612081; ap=965862351; t=6b103ee54913c5f777b26846260512731; societyguester=6b103ee54913c5f777b26846260512731; id=965862351; xnsid=10c3bb4e; l"
             "oginfrom=syshome; jebe_key=acc0eb83-284d-4293-9023-66158f48cdeb%7C635202bd88a78cd7a4d52afd43f370f1%7C1533025135601%7C1"
}

req=request.Request(url=dapeng_url,headers=headers)

resp=request.urlopen(req)
# print(resp.read().decode('UTF-8'))
with open("renren.html","w",encoding=('UTF-8')) as fp:
    #witer函数必须写入一个str的数据类型
    #resp.read()读出来的是一个bytes数据类型
    #bytes -> decode->str
    #  str-> decode->bytes
    fp.write(resp.read().decode('UTF-8'))

