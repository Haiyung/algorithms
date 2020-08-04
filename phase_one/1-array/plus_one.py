# Source : https://leetcode-cn.com/problems/plus-one/
# Author : Haiyung
# Date   : 2020-07-16

'''
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位，数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
'''

# 暴力翻译：将数组转为数字，数字加一，将数字转为字符串，将字符串转为数组，将字符串类型的数组转为数字类型的数组

def plus_one(nums):
    num = 0
    length = len(nums)
    for i in range(length):
        v = nums[i]
        num += pow(10, length - 1 - i) * v
    num += 1

    ret = list(str(num))
    for i in range(len(ret)):
        ret[i] = int(ret[i])
    return ret


print(plus_one([1, 2, 3]))
