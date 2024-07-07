# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

####################################
#   Dec 2023
####################################
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        count_a = self.countList(headA)
        count_b = self.countList(headB)

        gap = count_a - count_b

        while gap != 0:
            if gap > 0:
                headA= headA.next
                gap -= 1
            elif gap < 0:
                headB = headB.next
                gap += 1
        nodes_left = count_a if count_a < count_b else count_b

        for i in range(nodes_left):
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next

        return None

    def countList(self, head):
        count = 0
        while head:
            count += 1
            head = head.next

        return count