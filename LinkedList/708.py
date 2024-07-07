from typing import Optional


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':

        if not head:
            curr = Node(insertVal)
            curr.next = curr
            return curr
        if head.next == head:
            head.next = Node(insertVal, head)
            return head

        prev, cur = head, head.next

        while (not prev.val <= insertVal <= cur.val) and cur != head:
            if prev.val > cur.val and (insertVal > prev.val or insertVal < cur.val):
                break
            prev = cur
            cur = cur.next

        prev.next = Node(insertVal, cur)

        return head

h1 = Node(1)
h4 = Node(4, h1)
head = Node(3, h4)
h1.next = head

res = Solution().insert(head, 2)
print(res.val)
cur = res.next
while cur != res:
    print(cur.val)
    cur = cur.next
