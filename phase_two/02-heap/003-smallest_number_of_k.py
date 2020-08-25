# Source : https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/
# Author : Haiyung
# Date   : 2020-07-29

'''
最小的k个数

输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例：
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

限制：
0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000
'''

# sort 排序 NlogN
# heap
# quick-sort

import heapq
from typing import List
import copy


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        '''大根堆'''
        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans

    def getLeastNumbersTest(self, arr: List[int], k: int) -> List[int]:
        '''小根堆'''
        if k == 0:
            return list()
        elif k >= len(arr):
            return arr

        a = copy.deepcopy(arr)
        ret = list()
        heapq.heapify(a)
        for i in range(k):
            ret.append(a[0])
            heapq.heappop(a)
        return ret


so = Solution()
# arr = so.getLeastNumbers([9, 54, 23, 44], 2)
arr = so.getLeastNumbersTest([9, 54, 23, 44], 2)
print(arr)
