# 高级排序
# 归并排序 Merge Sort => O(N*LogN)
# 1. 把长度为n的输入序列分成两个长度为n/2的子序列
# 2. 对这两个子序列分别采用归并排序
# 3. 将两个排序好的子序列合并成一个最终的排序序列


def mergesort(nums, left, right):
    if right <= left:
        return
    mid = (left+right) >> 1
    mergesort(nums, left, mid)
    mergesort(nums, mid+1, right)
    merge(nums, left, mid, right)


def merge(nums, left, mid, right):
    temp = []
    i = left
    j = mid+1
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1
    while i <= mid:
        temp.append(nums[i])
        i += 1
    while j <= right:
        temp.append(nums[j])
        j += 1
    nums[left:right+1] = temp
