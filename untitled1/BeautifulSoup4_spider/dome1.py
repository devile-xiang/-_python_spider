#encoding=utf-8

from bs4 import BeautifulSoup
html="""
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1" id="ko"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>


"""

soup=BeautifulSoup(html,"lxml")
#获取所有的；li
# allli=soup.find_all("li")
# for i in allli:
#     print(i)
#获取第二个人li
# lis=soup.find_all('li',limit=2)[1]
# print(lis)

#获取class 等于item-1
#class_='item-1'
# lis=soup.find_all('li',attrs={'class':'item-1'})
# for i in lis:
#     print(i)

#获取class 等于item-1 并且id=ko
# lis=soup.find_all('li',attrs={'id':'ko','class':'item-1'})
# print(lis)

#获取所有a标签的href属性
#
# ass = soup.find_all('a')
# for i in ass:
#     print(i['href'])

#获取所有的文本信息纯文本
# trs=soup.find_all('li')[1:]
# for tr in trs:
#     tds=tr.find_all("a")
#     text=tds[0]
#     print(text.string)
#

