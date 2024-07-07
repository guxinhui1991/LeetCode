# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def findSmallestNode(self, head):
        if not head: return _, head

        min_val = head.val
        min_node = head
        while head:
            if head.val < min_val:
                min_val = head.val
                min_node = head
                head = head.next
        return min_val, min_node

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head: return

        dummy = ListNode(0, head)
        cur = ListNode(0, head)


        while cur and cur.next:
            if cur.val < cur.next.val:
                cur = cur.next
                continue
            else:
                temp = cur.next
                cur.next = cur.next.next
                prev = dummy
                while prev.next.val <= temp.val:
                    prev = prev.next

                temp.next = prev.next
                prev.next = temp



        return dummy.next