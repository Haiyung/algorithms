# Source : https://leetcode-cn.com/problems/combinations/
# Author : Haiyung
# Date   : 2020-08-04


'''
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''


def combine(n, k):
    ret = list()
    if n <= 0 or k <= 0 or n < k:
        return ret
    else:
        pass
