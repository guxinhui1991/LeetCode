# Definition for singly-linked list.

#class Solution(object):
#    def deleteDuplicates(self, head):
#        """
#        :type head: ListNode
#        :rtype: ListNode
#        """
#        if(head==None):
#            return head
#        while(head.next):
#            if(head.next.val == head.val):
#                head.next = head.next.next
#        return head
    
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next     # skip duplicated node
            cur = cur.next     # not duplicate of current node, move to next node
        return head
    
print(Solution().deleteDuplicates([1]))