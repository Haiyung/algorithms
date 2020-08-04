# Source : https://leetcode-cn.com/problems/two-sum/
# Author : Haiyung
# Date   : 2020-07-09

'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''


def two_sum(nums, target):
    '''首先想到的解法是「暴力破解」'''
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


print(two_sum([2, 7, 11, 15], 9))


def two_sum_better(nums, target):
    '''其次的解法是: 选中一值后，看 target - num[i] 的值是否在 i 的位置之前出现过'''
    lens = len(nums)
    j = -1
    for i in range(1, lens):
        temp = nums[:i]
        if (target - nums[i]) in temp:
            j = temp.index(target - nums[i])
            break
    if j >= 0:
        return [j, i]


print(two_sum_better([2, 7, 11, 15], 9))
