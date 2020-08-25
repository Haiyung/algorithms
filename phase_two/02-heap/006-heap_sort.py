# Source : https://www.geeksforgeeks.org/heap-sort/
#          https://www.youtube.com/watch?v=j-DqQcNPGbE
# Author : Haiyung
# Date   : 2020-07-29

'''
堆排序
'''


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def heapify(tree, n, i):
    '''让某个子树堆化'''
    if i >= n:
        return
    left = 2 * i + 1
    right = 2 * i + 2
    max_node = i
    if (left < n and tree[left] > tree[max_node]):
        max_node = left

    if (right < n and tree[right] > tree[max_node]):
        max_node = right

    if max_node != i:
        swap(tree, max_node, i)
        heapify(tree, n, max_node)


arr = [4, 10, 3, 5, 1, 2]
n = 6
heapify(arr, n, 0)
print(arr)


def parent(i):
    return int((i - 1) / 2)


def build_heap(arr):
    '''把无序数组调整为堆'''
    last_one_index = len(arr) - 1
    p = parent(last_one_index)

    i = p
    while i >= 0:
        heapify(arr, len(arr), i)
        i -= 1


arr = [5, 1, 4, 10, 2, 3]
build_heap(arr)
print(arr)


def heap_sort(tree):
    '''有了堆之后做堆排序'''
    build_heap(tree)
    i = len(tree) - 1
    while i >= 0:
        swap(tree, i, 0)
        heapify(tree, i, 0)
        i -= 1


arr = [5, 1, 4, 10, 2, 3]
heap_sort(arr)
print(arr)
