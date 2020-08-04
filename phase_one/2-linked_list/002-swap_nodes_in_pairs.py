# Source : https://leetcode-cn.com/problems/reverse-linked-list/
# Author : Haiyung
# Date   : 2020-07-10

'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
'''


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


def iterator_linked_list(head: ListNode) -> list:
    val = []
    tmp = head
    while tmp:
        if tmp.val != None:
            val.append(tmp.val)
        tmp = tmp.next
    return val


def swap_pairs(head: ListNode) -> ListNode:
    if not head:
        return

    result = ListNode(0)
    result.next = head
    father = result

    first, second = head, head.next
    while first and second:
        first.next = second.next
        second.next = first
        first, second = second, first
        father.next = first
        first = first.next.next
        second = second.next.next
        father = father.next.next

    return result.next


linked_list_test_01 = CreatSinglyLinkedList([1, 2, 3, 4, 5, 6, 7])
sp = swap_pairs(linked_list_test_01.head)
print(iterator_linked_list(sp))
