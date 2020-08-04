# Source : https://leetcode-cn.com/problems/valid-parentheses/
# Author : Haiyung
# Date   : 2020-07-17

# 问：什么问题适合用“栈”来解决？
# 如果一个东西具有最近相关性，就适合用栈来解决
# 最近相关性指的是：像洋葱一样，从外向内或者从内向外逐渐扩散，是一对一对出现的。

# 而讲究公平性的(先来后到)的问题，就适合用队列来解决。


'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    注意空字符串可被认为是有效字符串。
'''


def is_valid(s) -> bool:
    stack = []

    dic = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    for v in s:
        if v in dic:
            stack.append(v)
        else:
            if len(stack) == 0 or dic[stack.pop()] != v:
                return False

    return len(stack) == 0


s = '()[]()[]'
print(is_valid(s))
