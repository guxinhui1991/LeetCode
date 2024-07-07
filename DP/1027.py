from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        N = len(nums)
        res = 2
        dp =[[1 for _ in range(1000)] for _ in range(N)]
        for r in range(N):
            for l in range(0, r):
                d = nums[r] - nums[l]
                dp[r][d] = dp[l][d] + 1
                res = max(res, dp[r][d])

        return res