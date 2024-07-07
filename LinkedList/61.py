# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0: return head

        tail = ListNode(0, head)
        start = head

        count = 0
        while (head):
            tail = head
            count += 1
            head = head.next

        head = start
        if k % count == 0:
            return head

        else:
            tail.next = start
            k = k % count
            for i in range(count - k - 1):
                head = head.next

            res = head.next
            head.next = None

            return res

l5 = ListNode(5)
l4 = ListNode(4, l5)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)
k = 2
Solution().rotateRight(l1, k)

l1 = ListNode(1)
k = 1
Solution().rotateRight(l1, k)