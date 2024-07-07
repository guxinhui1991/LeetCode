# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_len(node):
            res = 0
            while node:
                res += 1
                node = node.next

            return res

        cur_len = get_len(head)
        steps = cur_len//2

        cur = head
        for _ in range(steps):
            cur = cur.next

        return cur


    # slow and fast pointers
    def middleNode2(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

