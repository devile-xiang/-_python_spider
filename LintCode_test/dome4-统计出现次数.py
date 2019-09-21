#encoding:utf-8



def main(n,k):
    print("N的值是%s"%n)
    narray = []
    for i in range(0, n+1):
        narray.append(i)
    print("要统计的次数是：%d"%n)
    print(narray)
    global a
    a=0

    if type(narray)==int:
        print("只有一个数")
        for j in str(narray):
            print(j)
            if j == str(k):
                a = a + 1
    else:
        #多个数
        for i in narray:
            for j in str(i):
                print(j)
                if j==str(k):
                    a=a+1
    if a==0:
        a=a+1

    print("%d总共出现了%d"%(k,a))





if __name__ == '__main__':

    n=12



    k=1
    main(n ,k)

