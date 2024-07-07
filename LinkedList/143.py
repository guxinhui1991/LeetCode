# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        temp = head
        count = 0
        cur_stack = []
        while temp:
            cur_stack.append(temp)
            temp = temp.next
            count += 1

        prev, curr = head, head.next
        for i in range((count - 1) // 2):
            node = cur_stack.pop()
            prev.next = node
            cur_stack[-1].next = node.next
            node.next = curr

            prev = curr
            curr = curr.next

        return head




