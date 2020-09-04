// 高级排序
// 归并排序 Merge Sort => O(N*LogN)
// 1. 把长度为n的输入序列分成两个长度为n/2的子序列
// 2. 对这两个子序列分别采用归并排序
// 3. 将两个排序好的子序列合并成一个最终的排序序列


const mergeSort = (nums) => {
    if (nums.length <= 1) return nums
    let mid = Math.floor(nums.length / 2),
        left = nums.slice(0, mid),
        right = nums.slice(mid)
    return merge(mergeSort(left), mergeSort(right))
}

const merge(left, right) => {
    let result = []
    while (left.length && right.length) {
        result.push(left[0] <= right[0] ? left.shift() : right.shift()
    }
    while (left.length) result.push(left.shift())
    while (right.length) result.push(right.shift())
    return result
}