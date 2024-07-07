import bisect
import collections
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = float('inf')

        N = len(nums)
        l = r = 0
        cur = 0
        while l < N:
            if nums[l] > 0:
                r = max(r, l)
                while r < N and cur < k:
                    cur += nums[r]
                    r += 1
                if cur >= k: res = min(res, r - l)

            cur -= nums[l]
            l += 1

        return -1 if res == float('inf') else res

    # deque method
    def shortestSubarray2(self, nums: List[int], k: int) -> int:
        N = len(nums)
        res = float('inf')
        d = collections.deque()

        cur_sum = [0] * (N + 1)
        for i in range(N):
            cur_sum[i + 1] = cur_sum[i] + nums[i]

        for i in range(N + 1):
            while d and cur_sum[i] - cur_sum[d[0]] >= k:
                res = min(res, i - d.popleft())

            while d and cur_sum[i] <= cur_sum[d[-1]]:
                d.pop()

            d.append(i)

        return -1 if res == float('inf') else res


print(Solution().shortestSubarray2([84, -37, 32, 40, 95], 167))
print(Solution().shortestSubarray2([-2, 7, -1, 4, -1], 10))
