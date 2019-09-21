#encoding:utf-8

#返回第二大的数
def secondMax():
    # write your code here

    nums = [1, 3, 5, 4]
    # global nums
    onemax= max(nums)
    # print(onemax)
    for item in range(len(nums)):
        if onemax == nums[item]:
            nums.pop(item)
            twomax = max(nums)
            return twomax

        # TODO: write code...



if __name__ == '__main__':

    twomax=secondMax()
    print(twomax)