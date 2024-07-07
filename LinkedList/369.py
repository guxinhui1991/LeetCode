# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:


    def plusOne_stack(self, head: ListNode) -> ListNode:

        if not head: return
        dummy = ListNode(0, head)
        curr = head
        roll = True
        stack = []
        while curr:
            stack.append(curr)
            curr = curr.next

        while roll:
            if stack:
                curr = stack.pop()
                roll = (curr.val + 1) == 10
                curr.val = (curr.val + 1) % 10
            else:
                break
        if roll:
            dummy.val += 1
            return dummy
        else:
            return dummy.next

    def plusOne(self, head: ListNode) -> ListNode:
        # sentinel head
        sentinel = ListNode(0)
        sentinel.next = head
        not_nine = sentinel

        # find the rightmost not-nine digit
        while head:
            if head.val != 9:
                not_nine = head
            head = head.next

        # increase this rightmost not-nine digit by 1
        not_nine.val += 1
        not_nine = not_nine.next

        # set all the following nines to zeros
        while not_nine:
            not_nine.val = 0
            not_nine = not_nine.next

        return sentinel if sentinel.val else sentinel.next