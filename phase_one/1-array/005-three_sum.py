# Source : https://leetcode-cn.com/problems/3sum/
# Author : Haiyung
# Date   : 2020-07-09

'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''

# 1. 三重循环后去重处理 => third nested loops
# 2. 利用哈希表的O(1)时间复杂度特性，代替一重循环，使得时间复杂度降至O(n^2)
# 3. 双指针法，或称左右夹逼 => two pointers


def three_sum_test_1(nums):
    '''三重循环-暴力求解'''
    nums.sort()  # sort 的时间复杂度是 nlog(n)
    ret = []
    for i in range(len(nums)):
        num_first = nums[i]
        if num_first > 0:
            continue
        for j in range(i+1, len(nums)):
            num_second = nums[j]
            for k in range(j+1, len(nums)):
                num_last = nums[k]
                if num_second + num_last == -num_first:
                    item = [num_first, num_second, num_last]
                    if item not in ret:
                        ret.append(item)
    return ret


print(three_sum_test_1([-1, 0, 1, 2, -1, -4, 0]))


def three_sum_test_2(nums):
    '''双指针法'''
    nums.sort()  # 1. sort 预处理
    ret = []
    for k in range(len(nums)-2):
        num_first = nums[k]
        if num_first > 0:
            break
        if k > 0 and nums[k] == nums[k - 1]:
            continue
        i, j = k + 1, len(nums) - 1
        while i < j:
            s = nums[k] + nums[i] + nums[j]
            if s < 0:
                i += 1
                while i < j and nums[i] == nums[i - 1]:  # 2. 去重处理
                    i += 1
            elif s > 0:
                j -= 1
                while i < j and nums[j] == nums[j + 1]:  # 2. 去重处理
                    j -= 1
            else:
                ret.append([nums[k], nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i - 1]:  # 2. 去重处理
                    i += 1
                while i < j and nums[j] == nums[j + 1]:  # 2. 去重处理
                    j -= 1
    return ret


# [-4, -1, -1, 0, 0, 1, 2] [-1, 0, 1, 2, -1, -4, 0]
print(three_sum_test_2([-1, 0, 1, 2, -1, -4, 0]))
