# Source : https://leetcode-cn.com/problems/reverse-linked-list/
# Author : Haiyung
# Date   : 2020-07-10

'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
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


def reverse_list_test_1(head: ListNode) -> ListNode:
    val = []
    head_val = head.val
    if head_val != None:
        val.append(head.val)
    tmp = head
    while tmp.next:
        next_one = tmp.next
        val.append(next_one.val)
        tmp = next_one
    val.reverse()

    if len(val) != 0:
        head.val = val[0]
    t = head
    for i in val[1:]:
        node = ListNode(i)
        t.next = node
        t = node
    return head


def iterator_linked_list(head: ListNode) -> list:
    val = []
    tmp = head
    t = 0
    while tmp:
        if tmp.val != None:
            val.append(tmp.val)
        tmp = tmp.next
        print(tmp)
        t += 1
        if t > 11:
            break

    return val


linked_list = CreatSinglyLinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
reversed_list = reverse_list_test_1(linked_list.head)
# print(iterator_linked_list(reversed_list))


def reverse_list_test_2(head: ListNode) -> ListNode:
    pre = ListNode(None)
    current = head

    while current:
        tmp = current.next
        current.next = pre
        pre = current
        current = tmp
    return pre


linked_list_2 = CreatSinglyLinkedList([1, 2, 3])
reversed_list_2 = reverse_list_test_2(linked_list_2.head)
print(iterator_linked_list(reversed_list_2))
