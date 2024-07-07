# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(float('inf'), head)
        prev, cur = dummy, head

        res = [dummy]
        while (cur):
            while (res and cur.val > res[-1].val):
                res.pop()
            res[-1].next = cur
            res.append(cur)
            cur = cur.next

        return dummy.next


l5 = ListNode(8)
l4 = ListNode(3, l5)
l3 = ListNode(13, l4)
l2 = ListNode(2, l3)
l1 = ListNode(5, l2)

Solution().removeNodes(l1)