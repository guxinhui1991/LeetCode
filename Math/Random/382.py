# Definition for singly-linked list.
import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.l = head
        cur_len = 0

        while head:
            cur_len += 1
            head = head.next
        self.length = cur_len

    def getRandom(self) -> int:
        idx = int(random.uniform(0, self.length))
        head = self.l
        while idx:
            head = head.next
            idx -= 1

        return head.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()