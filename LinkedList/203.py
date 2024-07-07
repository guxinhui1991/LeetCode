# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

####################################
#   Dec 2023
####################################
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        dummy = ListNode(next=head)
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next

def print_list(head):
    node = head
    while node:
        print(node.val)
        node = node.next


l7 = ListNode(7)
l6 = ListNode(7, l7)
l5 = ListNode(7, l6)
l4 = ListNode(7, l5)
l3 = ListNode(7, l4)
l2 = ListNode(7, l3)
l1 = ListNode(7, l2)

Solution().removeElements(l1, 7)
print_list(l1)
print('-----------')


l7 = ListNode(6)
l6 = ListNode(5, l7)
l5 = ListNode(4, l6)
l4 = ListNode(3, l5)
l3 = ListNode(6, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)

Solution().removeElements(l1, 6)
print_list(l1)