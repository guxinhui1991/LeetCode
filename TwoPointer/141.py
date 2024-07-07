from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head
        f = s.next if head else None

        while f and f.next:
            if s == f or s == f.next: return True
            s = s.next
            f = f.next.next

        return False

