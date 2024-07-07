from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        res, N = 0, len(nums)
        cur_count = {}
        r = 0
        for i, val in enumerate(nums):
            #cur_count[val] = cur_count.get(val, 0) + 1
            while r < N and cur_count.get(nums[r], 0)+1 <= k:
                cur_count[nums[r]] = cur_count.get(nums[r], 0) + 1
                r += 1

            res = max(res, r-i)

            cur_count[val] -= 1
        return res


print(Solution().maxSubarrayLength(nums = [1, 1, 1, 3] ,k = 2))
print(Solution().maxSubarrayLength(nums = [1,2,3,1,2,3,1,2], k = 2))
print(Solution().maxSubarrayLength(nums = [5,5,5,5,5,5,5], k = 4))
print(Solution().maxSubarrayLength(nums = [1,2,1,2,1,2,1,2], k = 1))