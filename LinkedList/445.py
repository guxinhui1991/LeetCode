# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        stack1, stack2 = [], []

        curr = l1
        while curr:
            stack1.append(curr)
            curr = curr.next
        curr = l2
        while curr:
            stack2.append(curr)
            curr = curr.next

        prevNode, nextNode = ListNode(0), ListNode(0)
        rollover = False
        while stack1 or stack2:
            cur_val, s1, s2 = 0, 0, 0
            if stack1: s1 = stack1.pop().val
            if stack2: s2 = stack2.pop().val
            cur_val = (s1 + s2 + nextNode.val) % 10
            rollover = (s1 + s2 + nextNode.val) // 10

            nextNode.val = cur_val
            prevNode.next = nextNode
            prevNode.val = rollover

            nextNode = prevNode
            prevNode = ListNode(0, nextNode)

        return nextNode if rollover else nextNode.next

l1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
l2 = ListNode(5, ListNode(6, ListNode(4)))
Solution().addTwoNumbers(l1, l2)