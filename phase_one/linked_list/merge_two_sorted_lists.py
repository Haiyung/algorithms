# Source : https://leetcode-cn.com/problems/merge-two-sorted-lists/
# Author : Haiyung
# Date   : 2020-07-16

'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''

# 暴力解法：三个指针，分别指向返回链表的当前节点、两个原链表比较的节点，选取最小值插入进返回节点
# 递归


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


linked_list_1 = CreatSinglyLinkedList([1, 2, 4])
linked_list_2 = CreatSinglyLinkedList([1, 3, 4])


def merge_two_lists_test_01(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    dummy_node = ListNode(0)
    head = dummy_node
    while (l1 and l2):
        if l1.val <= l2.val:
            head.next = ListNode(l1.val)
            l1 = l1.next
        else:
            head.next = ListNode(l2.val)
            l2 = l2.next
        head = head.next
    if l1 == None:
        head.next = l2
    if l2 == None:
        head.next = l1
    return dummy_node.next


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 == None:
        return l2
    if l2 == None:
        return l1

    if l1.val <= l2.val:
        master_branch = l1
        master_branch.next = merge_two_lists(l1.next, l2)
    else:
        master_branch = l2
        master_branch.next = merge_two_lists(l1, l2.next)
    return master_branch


linked_list_3 = merge_two_lists(linked_list_1.head, linked_list_2.head)
print(iterator_linked_list(linked_list_3))
