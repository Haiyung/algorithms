# Source : https://leetcode-cn.com/problems/move-zeroes/
# Author : Haiyung
# Date   : 2020-07-05

'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
'''

nums = [0, 1, 0, 3, 0, 0, 12]


# time-complexity: O(n^3)
# space-complexity: O(1)
def move_zeroes(nums):
    for index in range(len(nums)):
        if nums[index] != 0:
            for inside_index in range(index):
                if nums[inside_index] == 0:
                    nums[index], nums[inside_index] = nums[inside_index], nums[index]
                    break


move_zeroes(nums)
print(nums)


numbers = [1, 0, 0, 3, 12, 17, 0, 0, 0, 0, 0, 99]


# time-complexity: O(n)
# space-complexity: O(1)
def move_zeroes_test(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i]:
            nums[j] = nums[i]
            j += 1

    for i in range(j, len(nums)):
        nums[i] = 0


move_zeroes_test(numbers)
print(numbers)


# 师夷长技以制夷
# 第一种方法：COUNT ZERO: loop, count zeroes, move
# 第二种方法：COUNT NOT ZERO: index

numbers_test = [9, 9, 0, 1, 0, 3, 12]


def move_zeroes_test_2(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count += 1
        else:
            nums[i-count] = nums[i]

    for i in range(len(nums)-count, len(nums)):
        nums[i] = 0


move_zeroes_test_2(numbers_test)
print(numbers_test)

best_numbers_test = [9, 9, 0, 1, 0, 3, 12]


def move_zeroes_best(nums):
    not_zero_count = 0
    for index in range(len(nums)):
        if nums[index] != 0:
            nums[not_zero_count], nums[index] = nums[index], nums[not_zero_count]
            not_zero_count += 1


move_zeroes_best(best_numbers_test)
print(best_numbers_test)
