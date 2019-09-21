#coending:utf-8

import re


#1.匹配某个字符串
# text='hello'
# ret=re.match('he',text)
# print(ret.group())
#2.点，匹配任意的字符,不能匹配换行符
# text='hello'
# ret=re.match('.',text)
# print(ret.group())
#2.点，匹配任意的数字
text='125556'
ret=re.match('\d+',text)
print(ret.group())
#2.点，匹配任意的非数字
# text='+'
# ret=re.match('\D',text)
# print(ret.group())
# #2.点，匹配空白字符\r\n\t
# text='\r'
# ret=re.match('\s',text)
# print(ret.group())

#2.点，匹配的是大小写的字母和数字
# text='Z'
# ret=re.match('\w',text)
# print(ret.group())

#2.点，\W与\w相反
# text='++*-'
# ret=re.match('\W',text)
# print(ret.group())

#组合方式，只要满足中括号中的字符就可以匹配+匹配多个
# text='0256-89888989'
# ret=re.match('[\d\-]+',text)
# print(ret.group())

#以中括号的形式代替\d,^上尖括号，排除
# text='a'
# ret=re.match('[^0-2]',text)
# print(ret.group())

#以中括号的形式代替\w,匹配除了a-zA-Z0-9，的字符^,-尖括号上
# text='_'
# ret=re.match('[a-zA-Z0-9]+',text)
# print(ret.group())

############匹配多个字符############################
# *可以匹配多个任意字符
# text='78115'
# ret=re.match('\d*',text)
# print(ret.group())

# +可以匹配1个或者多个字符
# text='asd8'
# ret=re.match('\w+',text)
# print(ret.group())

# +可以匹配1个或者多个字符
# text='asd8'
# ret=re.match('\w+',text)
# print(ret.group())

# ？可以匹配一个或者0个（要么只有一个）
# text="ad+89"
# ret=re.match('\w?',text)
# print(ret.group())

# {m},指定匹配多少个字符
# text="ad+89"
# ret=re.match('\w{2}',text)
# print(ret.group())

# {m，n},指定匹配m-n个字符
# text="assddasd"
# ret=re.match('\w{1,5}',text)
# print(ret.group())


############ 小案例 ############################
#验证手机案例：
# text="18523555617"
# # ret=re.match('1[14578]\d{9}',text)
# # print(ret.group())

#验证邮箱案例：
# text="2904633401@qq.com"
# ret=re.match('\w+@[a-z0-9]+\.[a-z]+',text)
# print(ret.group())

#验证URL案例：/s(匹配空白字符)
# text="http://www.baidu.com"
# ret=re.match('(http|https|ftp)://[^\s]+',text)
# print(ret.group())

#验证URL案例：/s(匹配身份证)
# text="50222154121234567X"
# ret=re.match('\d{17}[\dxX]',text)
# print(ret.group())


# 脱字号^,必须以h开始，放在中括号中，是取反的操作
# text="heallo"
# ret=re.search('^h',text)
# print(ret.group())


# $,是以...结尾,必须以@163.com结尾，不然会报错
# text="xxxx@163.com"
# ret=re.search('\w+@163.com$',text)
# print(ret.group())


# | ：匹配多个字符串或者表达式
# text="https54564"
# ret=re.search('(https|http)\d+',text)
# print(ret.group())


#贪婪模式和非贪婪模式
# text="0123456"
# ret=re.search('\d+?',text)
# print(ret.group())

#非贪婪模式
# text="<h1>标题</h1>"
# ret=re.search('<.+?>',text)
# print(ret.group())

#匹配0-100中的数字
#可以出现的：1,3,10,100,99
#不可以出现：09,101
#
# text="100"
# ret=re.match('[1-9]\d?$|100$',text)
# print(ret.group())

#使用转义字符 \$

# text=" hello world ,you need $299"
# ret=re.search('\$\d+',text)
# print(ret.group())

# text=r"\n"
# print(text)

# text="\\n"
# #pythond '\\n'=>\n
# #\\\\n=>\\n
# #要写四个反斜杠再能匹配一个\n
# ret=re.match('\\\\n',text)
# print(ret.group())





