from typing import List
from collections import deque


class MyQueue():
    def __init__(self):
        self.queue = deque()

    def pop(self, value):
        if self.queue and self.queue[0] == value:
            self.queue.popleft()

    def push(self, value):
        if not self.queue:
            self.queue.append(value)
            return
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    def front(self):
        return self.queue[0] if self.queue else None

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        cur_q = MyQueue()
        for i in range(k):
            cur_q.push(nums[i])
        res.append(cur_q.front())

        for i in range(k, len(nums)):
            cur_q.pop(nums[i-k])
            cur_q.push(nums[i])
            res.append(cur_q.front())

        return res

print(Solution().maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
print(Solution().maxSlidingWindow(nums = [1,3,1,2,0,5], k = 3))