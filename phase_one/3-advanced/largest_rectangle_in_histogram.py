# Source : https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
# Author : Haiyung
# Date   : 2020-07-17


def largest_rectangle_area_test_1(heights):
    '''暴力解法_1：
    时间复杂度：O(n^2)；
    空间复杂度：O(1)
    '''
    max_area = 0
    for i in range(len(heights)):
        height = heights[i]
        length = 1
        left = i - 1
        right = i + 1

        while left >= 0:
            if heights[left] < height:
                break
            length += 1
            left -= 1

        while right < len(heights):
            if heights[right] < height:
                break
            length += 1
            right += 1
        tmp = height * length
        if max_area < tmp:
            max_area = tmp
    return max_area


nums = [2, 1, 5, 6, 2, 3]
nums_1 = [2, 1, 2]
print(largest_rectangle_area_test_1(nums_1))


def largest_rectangle_area_test_2(heights):
    '''栈 => wrong answer
    时间复杂度：O(n)；
    空间复杂度：O(n)
    '''
    max_area = 0
    stack = []

    for i in range(len(heights)):
        if len(stack) == 0:
            stack.append(i)
            continue
        if heights[i] >= heights[stack[-1]]:
            stack.append(i)
            continue
        else:
            while len(stack) > 0 and heights[stack[-1]] > heights[i]:
                top = stack.pop()
                while len(stack) > 0 and heights[stack[-1]] == top:
                    top = stack.pop()

                area = heights[top] * (i - top)
                if max_area < area:
                    max_area = area

    return max_area


# print(largest_rectangle_area_test_2(nums_1))


def largest_rectangle_area_test_3(heights):
    '''单调栈
    时间复杂度：O(n)；
    空间复杂度：O(n)
    '''
    n = len(heights)
    left, right = [0] * n, [0] * n

    mono_stack = list()
    for i in range(n):
        while mono_stack and heights[mono_stack[-1]] >= heights[i]:
            mono_stack.pop()
        left[i] = mono_stack[-1] if mono_stack else -1
        mono_stack.append(i)

    mono_stack = list()
    for i in range(n - 1, -1, -1):
        while mono_stack and heights[mono_stack[-1]] >= heights[i]:
            mono_stack.pop()
        right[i] = mono_stack[-1] if mono_stack else n
        mono_stack.append(i)

    ans = max((right[i] - left[i] - 1) * heights[i]
              for i in range(n)) if n > 0 else 0
    return ans


# print(largest_rectangle_area_test_3(nums_1))


def largest_rectangle_area_test_4(heights):
    size = len(heights)
    res = 0

    stack = []

    for i in range(size):
        while len(stack) > 0 and heights[i] < heights[stack[-1]]:
            cur_height = heights[stack.pop()]

            while len(stack) > 0 and cur_height == heights[stack[-1]]:
                stack.pop()

            if len(stack) > 0:
                cur_width = i - stack[-1] - 1
            else:
                cur_width = i

            res = max(res, cur_height * cur_width)
        stack.append(i)

    while len(stack) > 0 is not None:
        cur_height = heights[stack.pop()]
        while len(stack) > 0 and cur_height == heights[stack[-1]]:
            stack.pop()

        if len(stack) > 0:
            cur_width = size - stack[-1] - 1
        else:
            cur_width = size
        res = max(res, cur_height * cur_width)

    return res


print(largest_rectangle_area_test_4(nums_1))
