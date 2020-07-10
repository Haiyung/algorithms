# Source : https://leetcode-cn.com/problems/climbing-stairs/
# Author : Haiyung
# Date   : 2020-07-09

'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶


示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

'''


# Fibonacci

def climb_stairs(num):
    if num == 1:
        return 1
    if num == 2:
        return 2

    a = [1, 1, 2]
    n = 3
    while n <= num:
        a.append(a[n-1] + a[n-2])
        n += 1
    return a[num]


print(climb_stairs(99))


def climb_stairs_standard(n):
    if n <= 2:
        return n
    f1, f2, f3 = 1, 2, 0
    for i in range(3, n+1):
        f3 = f2 + f1
        f1 = f2
        f2 = f3
    return f3


print(climb_stairs_standard(99))
