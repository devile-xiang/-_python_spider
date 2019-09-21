#encoding:utf-8

from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a> 
     </ul>
 </div>
'''

def parse_text():
    htmlElement=etree.HTML(text)
    print(etree.tostring(htmlElement,encoding='utf-8').decode('utf-8'))
def parse_file():
    htmlElement=etree.parse("tengxun.html")
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))


if __name__ == '__main__':
    parse_file()