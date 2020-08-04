# Source : https://leetcode-cn.com/problems/group-anagrams/
# Author : Haiyung
# Date   : 2020-07-23

'''
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

说明：
所有输入均为小写字母。
不考虑答案输出的顺序。
'''


def group_anagrams_test_1(strs):
    ret = list()
    comparison_list = list()

    for v in strs:
        tmp = "".join(sorted(v))
        if tmp not in comparison_list:
            comparison_list.append(tmp)
            ret.append([v])
        else:
            i = comparison_list.index(tmp)
            ret[i].append(v)

    return ret
