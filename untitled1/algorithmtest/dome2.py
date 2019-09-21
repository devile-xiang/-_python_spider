#encoding:utf-8

def maximumSwap(self, num):
    # Write your code here
    num=str(num)
    # print(len(num))
    nummax=(max(num))
    nums=[]
    for i in range(len(num)):
        # print(num[i])
        nums.append(num[i])
    for i in range(len(nums)):
        # print(nums[i])
        if nummax == nums[i]:
            nums.pop(i)
            # print(nums)
            nums.insert(0,nummax)
    print(nums)
    a=""
    for k in range(len(nums)):
        a=a+nums[k]

    lastnum=int(a)
    print(lastnum)
    return lastnum




if __name__ == '__main__':
    num=2736
    maximumSwap(self=num,num=num)
