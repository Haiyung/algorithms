# Source : https://leetcode-cn.com/problems/generate-parentheses/
# Author : Haiyung
# Date   : 2020-07-30


'''括号生成

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例：
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
'''

res = list()


def generate_parenthesis(left, right, n, s):
    if left == n and right == n:
        res.append(s)
        return

    if left < n:
        generate_parenthesis(left + 1, right, n, s + '(')
    if right < left:
        generate_parenthesis(left, right + 1, n, s + ')')


generate_parenthesis(0, 0, 3, '')
print(res)


# 根据以上的递归代码，我感觉到，递归有一个非常大的能力，就是能对规律的数据结构进行遍历(穷举)
