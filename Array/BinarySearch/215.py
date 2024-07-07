import random
from collections import deque
from typing import List

class MyQueue():
    def __init__(self):
        self.queue = deque()

    def pop(self, value):
        if self.queue and self.queue[0] == value:
            self.queue.popleft()

    def push(self, value, k):
        if not self.queue:
            self.queue.append(value)
            return
        tmp_q = []
        while self.queue and value > self.queue[-1]:
            tmp_q.append(self.queue.pop())
        self.queue.append(value)
        while tmp_q and len(self.queue) <= k:
            self.queue.append(tmp_q.pop())

    def front(self):
        return self.queue[0] if self.queue else None

    def get_index(self, i):
        return self.queue[i] if self.queue else None

class Solution(object):
    # Dec 2023
    def findKthLargest2023_slow(self, nums: List[int], k: int) -> int:
        cur_stack = MyQueue()
        for i in nums:
            cur_stack.push(i, k)
        return cur_stack.get_index(k-1)

    # QuickSelect Algorithm
    #
    # O(N) on average
    #
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def quickSelect(arr, k):
            pivot = random.choice(arr)
            l, m, r = [], [], []
            for v in arr:
                if v > pivot: l.append(v)
                elif v < pivot: r.append(v)
                else: m.append(v)

            if len(l) >= k: return quickSelect(l, k)
            elif len(l) + len(m) < k: return quickSelect(r, k - len(m) - len(l))
            return pivot

        return quickSelect(nums, k)

    def findKthLargest_heapq(self, nums: List[int], k: int) -> int:

        cur_dic = {}
        for i in nums:
            cur_dic[i] = cur_dic.get(i, 0) + 1

        import heapq
        q = []
        for v, freq in cur_dic.items():
            heapq.heappush(q, (-v, freq))

        while k > 0:
            val, freq = heapq.heappop(q)
            k -= freq

        return -val

    # Apr 2021
    def findKthLargest0(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        numMax = nums[0]
        numMaxIdx = 0
        for i in range(1, len(nums)):
            if nums[i] > numMax:
                numMax = nums[i]
                numMaxIdx = i

        if k == 1: return numMax
        else : return self.findKthLargest(nums[:numMaxIdx] + nums[numMaxIdx+1:], k-1)

    def findKthLargest1(self, nums, k):
        sortedNums = sorted(nums)
        return sortedNums[len(nums)-k]

import time

start_time = time.time()
print(Solution().findKthLargest0([3,2,1,5,6,4], 2))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(Solution().findKthLargest([3,2,1,5,6,4], 2))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(Solution().findKthLargest1([3,2,1,5,6,4], 2))
print("--- %s seconds ---" % (time.time() - start_time))
