# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dummy = ListNode(0)
        dummy.next = head

        nodes_list = []
        while dummy.next:
            if dummy.next not in nodes_list:
                nodes_list.append(dummy.next)
                dummy = dummy.next
            else:
                return False

        return True

l4 = ListNode(4)
l3 = ListNode(0, l4)
l2 = ListNode(2, l3)
l1 = ListNode(3, l2)
l4.next = l2

Solution().hasCycle(l1)
