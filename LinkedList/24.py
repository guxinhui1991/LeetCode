#Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


####################################
#   Apr 2023
####################################
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not (head and head.next): return head

        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while (curr and curr.next):
            nextFirst = curr.next
            nextSecond = curr.next.next

            # reverse
            prev.next = nextFirst
            nextFirst.next = curr
            curr.next = nextSecond

            # prepare for next loop
            prev, curr = curr, curr.next

        return dummy.next



####################################
#   Dec 2023
####################################
class Solution2(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head and head.next: return head
        dummy = cur = ListNode(head)

        while cur.next and cur.next.next:
            first, second = cur.next, cur.next.next
            cur.next = second
            first.next = second.next
            second.next = first

            cur = cur.next.next



        return dummy.next



l4 = ListNode(4)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)

Solution().swapPairs2(l1)