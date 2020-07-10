# Source : https://leetcode-cn.com/problems/container-with-most-water/
# Author : Haiyung
# Date   : 2020-07-06

'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。
'''


# 方法1. 遍历/枚举
# 方法2. 左右边界向中间收敛，即左右夹逼法

number = [1, 8, 6, 2, 5, 4, 8, 3, 7]


def max_area_test_1(nums):
    max = 0
    for out_index in range(len(nums)):
        for inside_index in range(out_index+1, len(nums)):
            min_height = nums[out_index] if nums[out_index] < nums[inside_index] else nums[inside_index]
            size = (inside_index - out_index) * min_height
            max = size if size > max else max
    return max


print(max_area_test_1(number))


def max_area_test_2(nums):
    max = 0
    start = 0
    end = len(nums) - 1
    while start < end:
        min_height = nums[start] if nums[start] < nums[end] else nums[end]
        size = (end - start) * min_height
        max = size if size > max else max
        if nums[start] < nums[end]:
            start += 1
        else:
            end -= 1
    return max


print(max_area_test_2(number))
