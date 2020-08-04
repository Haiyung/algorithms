# Source : https://leetcode-cn.com/problems/valid-anagram/
# Author : Haiyung
# Date   : 2020-07-23

'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

说明:
- 异位词：字母出现的次数是一样的；但顺序不一样
- 你可以假设字符串只包含小写字母。

示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
'''


# 1. 暴力解法：排序后相等
# 2. 哈希表

def is_anagram_1(s1, s2):
    return sorted(s1) == sorted(s2)


print(is_anagram_1("anagram", "nagaram"))


def is_anagram_2(s, t):
    if len(s) != len(t):
        return False
    m = dict()
    for v in s:
        if v in m:
            m[v] += 1
        else:
            m[v] = 1
    for v in t:
        if v in m:
            m[v] -= 1
        else:
            return False
    for v in m:
        if m[v] != 0:
            return False
    return True


print(is_anagram_2("an(agr*am我", "我na*ga(ram"))
