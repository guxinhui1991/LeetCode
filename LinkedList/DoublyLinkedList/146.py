class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.d = {}
        self.q = []
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        prev_end = self.tail.prev
        prev_end.next = node
        self.tail.prev = node
        node.prev = prev_end
        node.next = self.tail

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.d: return -1
        node = self.d[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])

        node = ListNode(key, value)
        self.add(node)
        self.d[key] = node
        if len(self.d) > self.c:
            node = self.head.next
            self.remove(node)
            del self.d[node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)