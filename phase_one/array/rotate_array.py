# Source : https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
# Author : Haiyung
# Date   : 2020-07-15


'''
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

说明:
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的 原地 算法。
'''

# 利用额外的数组
# 利用余数，双重循环
# 三次翻转，时间复杂度：O(n)，空间复杂度：O(1)
# 环状替换


def rotate_array_test_1(nums, k):
    length = len(nums)
    k %= len(nums)
    if k == 0:
        return nums
    origin_prefix = nums[:length-k]
    origin_suffix = nums[length-k:]
    origin_suffix.extend(origin_prefix)
    nums[:] = origin_suffix


test_numbers = [1, 2, 3, 4, 5, 6, 7]
rotate_array_test_1(test_numbers, 103)
print(test_numbers)

# Time complexity: n^2
# Space complexity: 1


def rotate_array_test_2(nums, k):
    k %= len(nums)

    for i in range(k):
        previous = nums[-1]
        for j in range(len(nums)):
            nums[j], previous = previous, nums[j]


# nums = [1, 2, 3, 4, 5, 6, 7]
# rotate_array_test_2(nums, 3)
# print(nums)
