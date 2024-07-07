from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        res, N = 0, len(nums)

        l = 0
        curr = 1
        for r, val in enumerate(nums):
            curr = curr * val
            while curr >= k:
                curr = curr // nums[l]
                l += 1
            res += r - l + 1

        return res


Solution().numSubarrayProductLessThanK([10,5,2,6], 100)