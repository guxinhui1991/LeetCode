# Definition for singly-linked list.
import heapq
from typing import Optional, List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        if not lists: return
        res = ListNode(0)

        tmp = []
        heapq.heapify(tmp)
        for i, l in enumerate(lists):
            if l: heapq.heappush(tmp, (l.val, i, l))

        if tmp:
            res.next = tmp[0][2]
            while True:
                val, _, curNode = heapq.heappop(tmp)
                if curNode.next:
                    nextNode = curNode.next
                    heapq.heappush(tmp, (nextNode.val, _, nextNode))
                if not tmp: break
                curNode.next = tmp[0][2]


        return res.next


#
#   Mar 2024 - Divide and conquer
class Solution2:
    def merge2Lists(self, l, r):
        dummy = ListNode(0)
        cur = dummy
        while l and r:
            if l.val<=r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l or r
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists: return None
        if len(lists) == 1: return lists[0]

        m = len(lists)//2
        l, r = self.mergeKLists(lists[0:m]), self.mergeKLists(lists[m:])

        return self.merge2Lists(l, r)

lists = [[]]
Solution().mergeKLists(lists)

l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

lists = [l1, l2]
print(Solution2().mergeKLists(lists))
