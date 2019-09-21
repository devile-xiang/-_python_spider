#encoding:utf-8


def getnum(nums,target):
    low=0
    high=len(nums)-1

    # while low <= high:
    #     mid=(low+high)//2
    #     if nums[mid]==mid:
    #         return mid
    #     elif nums[mid] > target:
    #         high=mid-1
    #     else:
    #         low=mid+1
    # return -1
    while low <= high:
        #// 双反斜杠是向下取整数
        mid=(low+high)//2
        if nums[mid] == target:
            while True:
                mid=mid-1
                if nums[mid] != target:
                    return mid+1


        elif nums[mid] < target:
            low=mid + 1
        else:
            high=mid - 1
    return -1


def main():
    nums=[1,4,4,5,7,7,8,9,9,10]
    target=1
    data=getnum(nums,target)
    print(data)


if __name__ == '__main__':
    main()