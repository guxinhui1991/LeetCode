# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head

        prev, curr = head, head.next
        cur_len = 1

        # prev -> cur
        def swapNode(prev, cur, num):
            head = prev

            for i in range(num):
                if not cur: break
                tmp = cur.next
                cur.next = prev

                prev = cur
                cur = tmp
            head.next = cur
            return prev

        def getLen(start, num):
            i = 1
            while start.next and i < num:
                start = start.next
                i += 1

            return i

        while curr:
            num_nodes = min(cur_len + 1, getLen(curr, cur_len + 1))
            if num_nodes % 2 == 0:
                prev.next = swapNode(curr, curr.next, min(cur_len, num_nodes))

            else:
                for i in range(cur_len):
                    if not curr.next: break
                    prev = curr
                    curr = curr.next

            prev = curr
            curr = curr.next
            cur_len += 1
        return head


head = ListNode(5, ListNode(2, ListNode(6)))
Solution().reverseEvenLengthGroups(head)