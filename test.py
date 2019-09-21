#encoding:utf-8
import re


def main():
    # a=['一','二','三','四']
    #
    # if len(a)<5:
    #     print("这个值为空")
    # else:
    #     print("这个值不为空")
    #
    # for i,str1 in enumerate(a):
    #     print(i,str1)
    a="asddasdassda8989555"
    b=re.search('\d+',a)
    print(b.group())

if __name__ == '__main__':
    main()