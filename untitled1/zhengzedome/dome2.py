#encoding:utf-8


import re

#分组每一组要加上一个括号（），第一个加上括号表示第一组：
# text = "apple price is $99,orange price is $10"
# ret = re.search('.*(\$[0-9]+).*(\$[0-9]+)',text)
# print(ret.group(0))
# print(ret.group(1))
# print(ret.group(2))
# print(ret.groups())
# ret = re.search(r".*(\$\d+).*(\$\d+)",text)
# print("\n")
# print(ret.group())
# print(ret.group(0))
# print(ret.group(1))
# print(ret.group(2))
# print(ret.groups())

#找出所有满足条件得，返回一个列表
#
# text = 'apple price $99 orange price $88'
# ret = re.findall('[0-9]+',text)
# print(ret)

#替换匹配到的字符
# text = 'apple price $99 orange price $88'
# ret = re.sub('[0-9]+','0',text)
# print(ret)
#替换实例
# html = """
# <div>
# <p>基本要求：</p>
# <p>1、精通HTML5、CSS3、 JavaScript等Web前端开发技术，对html5页面适配充分了解，熟悉不同浏览器间的差异，熟练写出兼容各种浏览器的代码；</p>
# <p>2、熟悉运用常见JS开发框架，如JQuery、vue、angular，能快速高效实现各种交互效果；</p>
# <p>3、熟悉编写能够自动适应HTML5界面，能让网页格式自动适应各款各大小的手机；</p>
# <p>4、利用HTML5相关技术开发移动平台、PC终端的前端页面，实现HTML5模板化；</p>
# <p>5、熟悉手机端和PC端web实现的差异，有移动平台web前端开发经验，了解移动互联网产品和行业，有在Android,iOS等平台下HTML5+CSS+JavaScript（或移动JS框架）开发经验者优先考虑；6、良好的沟通能力和团队协作精神，对移动互联网行业有浓厚兴趣，有较强的研究能力和学习能力；</p>
# <p>7、能够承担公司前端培训工作，对公司各业务线的前端（HTML5\CSS3）工作进行支撑和指导。</p>
# <p><br></p>
# <p>岗位职责：</p>
# <p>1、利用html5及相关技术开发移动平台、微信、APP等前端页面，各类交互的实现；</p>
# <p>2、持续的优化前端体验和页面响应速度，并保证兼容性和执行效率；</p>
# <p>3、根据产品需求，分析并给出最优的页面前端结构解决方案；</p>
# <p>4、协助后台及客户端开发人员完成功能开发和调试；</p>
# <p>5、移动端主流浏览器的适配、移动端界面自适应研发。</p>
# </div>
# """
# #以下方式就是把下面的标签去掉
# ret=re.sub('</?[a-zA-Z0-9]+>','',html)
# print(ret)
#分割方式：在字符串间距的类型，放在第一个位置，间距字符就是分割符
# text = "hello world ni hao"
# ret = re.split(''
#                '\W'#匹配每一段字符
#                '',text)
# print(ret)
text = "the number is 20.50"
#把你的正则表达式存储在R里面可以加注释,后面一定要加,re.VERBOSE，不然就会报错
r=re.compile(r"""
            \d+ #小数点前面的数
            \.? #小数点可有可无
            \d+ #小数点后面的数

""",re.VERBOSE)
ret=re.search(r,text)
print(ret.group())
