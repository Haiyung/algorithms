# Source : https://leetcode-cn.com/problems/min-stack/
# Author : Haiyung
# Date   : 2020-07-17

'''
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。
'''

# 辅助栈


class MinStack:

    def __init__(self):
        self.stack = []
        self.auxiliary_stack = [None]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.auxiliary_stack.append(min(x, self.auxiliary_stack[-1]))

    def pop(self) -> None:
        if len(self.stack) < 1:
            return None
        self.auxiliary_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        if len(self.stack) < 1:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        return self.auxiliary_stack[-1]
