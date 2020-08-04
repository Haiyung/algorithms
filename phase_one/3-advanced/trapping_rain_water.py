# Source : https://leetcode-cn.com/problems/trapping-rain-water/
# Author : Haiyung
# Date   : 2020-07-21


def trap_test_1(height):
    '''暴力解法
    时间复杂度：O(n^2)
    空间复杂度：O(1)
    '''
    if len(height) <= 2:
        return 0

    size = 0
    for i in range(1, len(height) - 1):
        center = height[i]
        left = i - 1
        left_max = height[left]
        while left >= 0:
            tmp = height[left]
            left_max = max(left_max, tmp)
            left -= 1

        right = i + 1
        right_max = height[right]
        while right <= len(height) - 1:
            tmp = height[right]
            right_max = max(right_max, tmp)
            right += 1

        if min(left_max, right_max) <= height[i]:
            continue
        else:
            size += min(left_max, right_max) - height[i]

    return size


# print(trap_test_1([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


def trap_test_2(height):
    if len(height) <= 2:
        return 0

    stack = []
    size = 0

    for i in range(len(height)):
        if len(stack) == 0:
            stack.append(i)
            continue
        top_in_stack = stack[-1]
        if height[i] <= height[top_in_stack]:
            stack.append(i)
            continue
        else:
            while len(stack) > 0 and height[i] > height[stack[-1]]:
                pop = stack.pop()
                while len(stack) > 0 and height[pop] == height[stack[-1]]:
                    pop = stack.pop()

                if len(stack) == 0:
                    break

                top_in_stack = stack[-1]
                area_height = min(height[top_in_stack],
                                  height[i]) - height[pop]
                size += area_height * (i - 1 - top_in_stack)
            stack.append(i)

        '''
        else:
            pop = stack.pop()
            while len(stack) > 0 and pop == stack[-1]:
                stack.pop()

            if len(stack) > 0:
                top_in_stack = stack[-1]
                area_height = min(top_in_stack, height[i]) - height[pop]
                size += area_height * (i - 1 - top_in_stack)
                if height[i] <= height[stack[-1]]:
                    stack.append(i)
                else:
                    while len(stack) > 0 and height[i] >= height[stack[-1]]:
                        pop = stack.pop()
                        top_in_stack = stack[-1]
                        area_height = min(
                            top_in_stack, height[i]) - height[pop]
                        size += area_height * (i - 1 - top_in_stack)
                        if height[i] <= height[stack[-1]]:
                            stack.append(i)
        '''

    return size


print(trap_test_2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
