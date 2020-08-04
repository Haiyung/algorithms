# Source : https://leetcode-cn.com/problems/linked-list-cycle-ii/
# Author : Haiyung
# Date   : 2020-07-15

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detect_cycle(head: ListNode) -> ListNode:
    tmp = set()
    
    a = head
    while a:
        if a in tmp:
            return a
        tmp.add(a)
        a = a.next
    return None
