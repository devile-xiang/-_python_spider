#encoding:utf-8

import requests
import re


HEADER={
    'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36',
    'accept-language':'zh-CN,zh;q=0.9'
}

def parse_page(url):
    response=requests.get(url,HEADER)
    text=response.content.decode('utf-8')
    # print(text),,re.DOTALL,允许.*，匹配换行符
    titles=re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>',text,re.DOTALL)
    Dynasty=re.findall(r'<p\sclass="source">.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    author=re.findall(r'<p\sclass="source">.*?<a.*?>.*?</a>.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    contents_tags=re.findall(r'<div class="contson".*?>(.*?)</div>',text,re.DOTALL)
    contents=[]
    for content in contents_tags:
        # print(content)
        x=re.sub(r'<.*?>',"",content)
        # print(x.strip())
        contents.append(x.strip())
    poems=[]
    for value in zip(titles,Dynasty,author,contents):
        title,Dynasty,author,content = value
        poem = {
            'title':title,
            'Dynasty':Dynasty,
            'author':author,
            'content':content
        }
        poems.append(poem)

    for poem in poems:
        print(poem)
        print('='*40)

def main():

    # url='https://www.gushiwen.org/default_1.aspx'
    for x in range(1,11):
        print("第%s页的数据"% x)
        url="https://www.gushiwen.org/default_%s.aspx"% x

        parse_page(url)

if __name__ == '__main__':
    main()