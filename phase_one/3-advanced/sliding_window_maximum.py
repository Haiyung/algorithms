# Source : https://leetcode-cn.com/problems/sliding-window-maximum/
# Author : Haiyung
# Date   : 2020-07-21


'''
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。

进阶：
你能在线性时间复杂度内解决此题吗？
'''


def max_sliding_window(nums, k):
    '''暴力解法
    时间复杂度：O(N*k)
    空间复杂度：O(N)
    '''
    if k < 0:
        return None
    if len(nums) <= k:
        return list(max(nums))
    ret = list()
    for i in range(k-1, len(nums)):
        first = nums[i - 2]
        second = nums[i - 1]
        third = nums[i]
        max_num = max(first, second, third)
        ret.append(max_num)
    return ret


print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
