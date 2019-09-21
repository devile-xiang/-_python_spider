#encoding:utf-8


def main(a):
    title=""
    maxstr=""
    for i in a:
        #判断小写
        if i.islower()==True:
            title=title+i
        else:
            maxstr=maxstr+i

    returnstr=title+maxstr
    return returnstr

if __name__ == '__main__':

    a="Ac"

    str =main(a)
    print(str)