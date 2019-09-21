#coending:utf-8

def test(self,a):
    # print(a)
    # for i in range(len(a)-1):
    #     for j in range(len(a)-i-1):
    #         if a[j]>a[j+1]:
    #             a[j],a[j+1]=a[j+1],a[j]
    # return a

    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
    # for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数
    #     for j in range(len(nums) - i - 1):  # ｊ为列表下标
    #         if nums[j] > nums[j + 1]:
    #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
    # return nums

    pass

a=[5,2,45,6,8,2,3,1]
a=test(self=" ",a=a)
print(a)