#encoding：utf-8


import queue


def coinProblem(n , m):
    a=n-m
    # print(type(n))
    # print(type(m))
    # print(type(a))
    # print("应找回 %d"% a)
    marray=[100,50,20,10,5,2,1]
    returnm=[]
    #超出时间太多，获取数据慢
    # while a!=0:
    #     for i in range(0, len(marray)):
    #         if (a - marray[i] >= 0):
    #             print("当前可取整数%d" % marray[i])
    #             returnm.append(marray[i])
    #             a = a - marray[i]
    #             break
    #
    # print(returnm)
    # print(len(returnm))
    # return (len(returnm))

    moneyNumber=0

    for i in range(0,len(marray)):
        print("当前货币%d"%marray[i])
        # print(a%100)
        if (a%marray[i] != 0):
            num1=a/marray[i]
            num=int(num1)

            print("%s的可以补：%d 张" %(marray[i],num))
            if num>0:
                moneyNumber=moneyNumber + num
            Surplus=num*marray[i]
            print("这次要减去%d" % Surplus)
            a=a-Surplus
            print("剩余：%d"% a)
        else:
            num1 = a / marray[i]
            Surplus=a-num1*marray[i]
            print("%d可以补%d张"% (marray[i],num1))

            if (num1> 0):
                moneyNumber=moneyNumber+num1
            print("最后剩余：%d"% Surplus)
            a=a-Surplus
            break

    print(moneyNumber)
    return int(moneyNumber)




def main():
    n = 100
    m = 29
    moneyNumber=coinProblem(n,m)
    print("最少可以找：%d"% moneyNumber)


if __name__ == '__main__':
    main()