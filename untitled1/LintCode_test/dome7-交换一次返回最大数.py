#encoding:utf-8

def maximumSwap(num):
    num=str(num)
    numarray=[]
    for i in num:
        numarray.append(i)
    maxnum=max(num)

    maxarray=[]

    for i in range(len(numarray)):
        maxnum1=max(numarray)
        if numarray[i]==maxnum:
            maxarray.append(numarray[i])
            numarray.remove(i)






        elif numarray[0] != maxarray:
            for i, k in enumerate(numarray):
                if k==maxnum:
                    print("他的下标是%s"%i)
                    index_i=i
            numarray[0],numarray[index_i]=numarray[index_i],numarray[0]
            break






    # print("最大值是%s"%maxnum)
    # index_i=""
    #
    # if numarray[0]==maxnum:
    #     pass
    #
    #
    # for i,k in enumerate(numarray):
    #     if k==maxnum:
    #         print("他的下标是%s"%i)
    #         index_i=i
    # numarray[0],numarray[index_i]=numarray[index_i],numarray[0]


    # numarray.remove(maxnum)
    # numarray.insert(0,maxnum)
    n=""
    for i in numarray:
       n=n+i
    print(n)

    n=int(n)

    return n


def main():
    # num=9986739
    num=5698
    num=maximumSwap(num=num)


    print("返回最大值是%s"%num)

if __name__ == '__main__':
    main()