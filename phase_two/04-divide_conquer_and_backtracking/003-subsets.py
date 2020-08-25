# Source : https://leetcode-cn.com/problems/subsets/
# Author : Haiyung
# Date   : 2020-08-25


'''
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。
'''


def subsets(nums):
    result = []
    if len(nums) == 0:
        return result
    dfs(result, nums, [], 0)
    return result


def dfs(result, nums, tmp, index):

    # terminator
    if index == len(nums):
        result.append(tmp)
        return

    # process logic
    dfs(result, nums, tmp.copy(), index + 1)

    t = tmp.copy()
    t.append(nums[index])
    dfs(result, nums, t, index + 1)


# p = subsets([1, 2, 3])
# print(p)


def subsets_II(nums):
    res = [[]]
    for i in nums:
        # list comprehension: Python 中经典的“列表推导式” -> 语法糖
        res = res + [[i] + num for num in res]
    return res


p = subsets_II([1, 2, 3])
print(p)
