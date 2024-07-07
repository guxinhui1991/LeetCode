# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

####################################
#   Dec 2023
####################################

# Counting
class Solution(object):
    def removeNthFromEnd(self, head, n):
        count = 0
        dummy = ListNode(next = head)
        cur = dummy
        while cur.next:
            count += 1
            cur = cur.next

        cur = dummy
        for i in range(count - n):
            cur = cur.next
        if n == 1:
            cur.next = None
        else:
            cur.next = cur.next.next
        return head




####################################
#   Dec 2023
####################################

# Fast Slow pointer
class Solution2(object):
    def removeNthFromEnd(self, head, n):

        fast = slow = dummy = ListNode(next = head)
        for _ in range(n + 1):
            fast = fast.next

        while fast and slow:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next




l5 = ListNode(5)
l4 = ListNode(4, l5)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)

Solution().removeNthFromEnd(l1, 2)