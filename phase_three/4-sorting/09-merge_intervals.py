# Source : https://leetcode-cn.com/problems/merge-intervals/
# Author : Haiyung
# Date   : 2020-09-04


'''合并区间

给出一个区间的集合，请合并所有重叠的区间。

示例 1:
    输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
    输出: [[1,6],[8,10],[15,18]]
    解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:
    输入: intervals = [[1,4],[4,5]]
    输出: [[1,5]]
    解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

提示：
    intervals[i][0] <= intervals[i][1]
'''
