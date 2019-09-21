#encoding:utf-8

import requests
import re

HEADER={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'
}
main_contents=[]
def page_content(url):
    response=requests.get(url)
    text=response.content.decode('utf-8')
    contents_1=re.findall(r'<div\sclass="content">(.*?)</div>',text,re.S)
    contents=[]
    for content in contents_1:
        x=re.sub(r'<.*?>',"",content)
        contents.append(x.strip())


    main_contents.append(contents)
    return main_contents





def main():


    for i in range(1,11):
        url = "https://www.qiushibaike.com/text/page/%s/"%i

        main_contents=page_content(url)
    for i in main_contents:
        for x in i:
            print(x)




if __name__ == '__main__':
    main();