# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

####################################
#   Apr 2023
####################################
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev, curr = None, head
        while(curr.next):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return curr

####################################
#   Dec 2023
####################################
class Solution2(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev, cur = None, head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev


l4 = ListNode(4)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)

Solution().reverseList(l1)