# Source : https://leetcode-cn.com/problems/linked-list-cycle/
# Author : Haiyung
# Date   : 2020-07-15


'''
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
'''

# 1. 利用额外数组，看下一个节点是否存在于数组中
# 2. 快慢指针
# 3. 改变原有节点的值，使每一个遍历过的节点都等于某个常数，看下一个节点是否等于某常数


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class CreatSinglyLinkedList:
    def __init__(self, data: list):
        self.head = ListNode(None)
        if len(data) != 0:
            self.head = ListNode(data[0])
        tmp = self.head
        for i in data[1:]:
            node = ListNode(i)
            tmp.next = node
            tmp = node


def has_cycle(head: ListNode) -> bool:
    slow, fast = head

    while slow and fast:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
