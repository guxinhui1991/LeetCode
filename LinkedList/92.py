# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev, cur = dummy, head

        for _ in range(left - 1):
            prev, cur = cur, cur.next

        ptr_l = prev

        prev = None

        for _ in range(right - left + 1):
            next_node = cur.next
            cur.next = prev
            prev, cur = cur, next_node

        ptr_l.next.next = cur
        ptr_l.next = prev

        return dummy.next
