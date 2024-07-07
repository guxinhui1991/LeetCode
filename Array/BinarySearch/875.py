import math
from typing import List


class Solution:
    # Exclusive boundaries
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles.sort(reverse=True)

        l, r = 1, max(piles)

        while l < r:
            m = l + (r - l) // 2

            cur_time = sum([math.ceil(i / m) for i in piles])
            # if cur_time == h : return m
            if cur_time <= h:
                r = m
            else:
                l = m + 1
        print (l, m, r)
        return r

    # Inclusive boundaries
    def minEatingSpeed2(self, piles: List[int], h: int) -> int:
        # piles.sort(reverse=True)

        l, r = 1, max(piles)

        while l <= r:
            m = l + (r - l) // 2

            cur_time = sum([math.ceil(i / m) for i in piles])
            # if cur_time == h : return m
            if cur_time <= h:
                r = m - 1
            else:
                l = m + 1
        print (l, m, r)
        return l

Solution().minEatingSpeed([3,6,7,11] , 8)
Solution().minEatingSpeed([30,11,23,4,20], 5)
Solution().minEatingSpeed([30,11,23,4,20], 6)
Solution().minEatingSpeed([312884470], 312884469)
Solution().minEatingSpeed([1,1,1,999999999], 10)