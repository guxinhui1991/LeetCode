import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        p_sum = 0
        self.prefix = []
        for v in w:
            p_sum += v
            self.prefix.append(p_sum)
        self.total = p_sum

    def pickIndex(self) -> int:
        t = random.randint(1, self.total)
        for i, v in enumerate(self.prefix):
            if v >= t:
                return i

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()