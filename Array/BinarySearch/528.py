import random
from typing import List


class Solution0:

    def __init__(self, w: List[int]):
        self.total = sum(w)
        self.weights = [w_i / self.total for w_i in w]

    def pickIndex(self) -> int:
        population = [i for i in range(len(self.weights))]
        prob = self.weights
        return random.choices(population, prob)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

class Solution1:

    def __init__(self, w: List[int]):
        self.res = [0 for _ in w]
        self.res[0] = w[0]
        for i in range(1, len(w)):
            self.res[i] = self.res[i - 1] + w[i]

    def pickIndex(self) -> int:
        target = int(random.uniform(0, self.res[-1])) + 1
        l, r = 0, len(self.res) - 1

        while l < r:
            mid = (l + r) // 2
            if self.res[mid] == target: return mid

            if self.res[mid] < target:
                l = mid + 1
            elif self.res[mid] > target:
                r = mid

        return l

