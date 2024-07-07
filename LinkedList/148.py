# Definition for singly-linked list.
import heapq
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:

    # Priority Queue method
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q = []
        heapq.heapify(q)
        while head:
            heapq.heappush(q, (head.val, head))
            head = head.next
        dummy = ListNode(0)
        dummy.next = q[0][0]
        while q:
            _, node = heapq.heappop(q)
            tmp = node
            tmp.next = q[0][1] if q else None

        return dummy.next


    


h = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
Solution().sortList(h)