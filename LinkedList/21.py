# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

####################################
#   Apr 2023
####################################
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = res = ListNode(0)

        while (list1 and list2):
            if list1.val < list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next
            res = res.next
        res.next = list1 or list2
        return dummy.next

####################################
#   Dec 2023
####################################
class Solution2(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0, next = list1 if list1.val < list2.val else list2)
        cur = dummy.next

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return dummy.next