import heapq
from typing import List


class Solution:

    # TLE
    def containsNearbyAlmostDuplicate0(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:

        for k in range(1, indexDiff + 1):
            if abs(nums[k] - nums[0]) <= valueDiff:
                return True

        N = len(nums)
        for i in range(1, N):
            l, r = i, i + 1
            while r <= indexDiff:
                if abs(nums[r] - nums[l]) <= valueDiff:
                    return True
                r += 1

        return False

    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:

        import bisect

        cur = []
        N = len(nums)

        for i in range(N):

            if i > indexDiff:
                cur.remove(nums[i - indexDiff - 1])

            l = bisect.bisect_left(cur, nums[i] - valueDiff)
            r = bisect.bisect_right(cur, nums[i] + valueDiff)

            if l != r and l!=len(cur): return True
            bisect.insort(cur, nums[i])

        return False

    def containsNearbyAlmostDuplicate2(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        from sortedcontainers import SortedSet

        cur = SortedSet()
        N = len(nums)

        for i in range(N):
            if i > indexDiff:
                cur.remove(nums[i - indexDiff - 1])

            idx1 = cur.bisect_left(nums[i] - valueDiff)
            if idx1 < len(cur) and abs(cur[idx1] - nums[i]) <= valueDiff:
                return True
            cur.add(nums[i])

        return False

print(Solution().containsNearbyAlmostDuplicate2(nums=[1,5,9,1,5,9], indexDiff=2, valueDiff=3))
print(Solution().containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], indexDiff=3, valueDiff=0))
print(Solution().containsNearbyAlmostDuplicate(nums=[1, 2, 3], indexDiff=1, valueDiff=10))
print(Solution().containsNearbyAlmostDuplicate(nums=[3, 6, 0, 4], indexDiff=2, valueDiff=2))
print(Solution().containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], indexDiff=3, valueDiff=0))
print(Solution().containsNearbyAlmostDuplicate(nums=[1, 5, 9, 1, 5, 9], indexDiff=2, valueDiff=3))
print(Solution().containsNearbyAlmostDuplicate(nums=[1, 2, 1, 1], indexDiff=1, valueDiff=0))
