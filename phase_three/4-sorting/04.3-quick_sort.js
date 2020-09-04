// 高级排序
// 快速排序 Quick Sort => O(N*LogN)
// 数组取标杆 pivot，将小元素放 pivot 左边，大元素放右侧，然后依次对右边和右边的子数组继续快排，以达到整个序列有序。


const quickSort = (nums, left, right) => {
    if (nums.length <= 1) return nums
    if (left < right) {
        index = partition(nums, left, right)
        quickSort(nums, left, index - 1)
        quickSort(nums, index + 1, right)
    }
}

const partition = (nums, left, right) => {
    let pivot = left, index = left + 1
    for (let i = index; i <= right; i++) {
        if (nums[i] < nums[pivot]) {
            [nums[i], nums[index]] = [nums[index], nums[i]]
            index++
        }
    }
    [nums[pivot], nums[index - 1]] = [nums[index - 1], nums[pivot]]
    return index - 1
}