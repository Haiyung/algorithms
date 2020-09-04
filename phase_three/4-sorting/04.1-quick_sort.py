# 高级排序
# 快速排序 Quick Sort => O(N*LogN)
# 数组取标杆 pivot，将小元素放 pivot 左边，大元素放右侧，然后依次对右边和右边的子数组继续快排，以达到整个序列有序。


def quick_sort(begin, end, nums):
    if begin >= end:
        return
    pivot_index = partition(begin, end, nums)
    quick_sort(begin, pivot_index-1, nums)
    quick_sort(pivot_index+1, end, nums)


def partition(begin, end, nums):
    pivot = nums[begin]
    mark = begin
    for i in range(begin+1, end+1):
        if nums[i] < pivot:
            mark += 1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark
