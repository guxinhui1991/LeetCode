from typing import List


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <=2: return max(nums)

        N = len(nums)
        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        dp[2] = max(nums[1], nums[0]+nums[2])
        for i in range(3, N):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])


        return dp[-1]

    def rob2(self, nums: List[int]) -> int:

        res = [0 for _ in range(len(nums)+1)]
        res[0], res[1] = 0, nums[0]
        for i in range(1, len(nums)+1):
            if nums[i-1] + res[i-2] >= res[i-1]:
                res[i] = nums[i-1] + res[i-2]
            else:
                res[i] = res[i - 1]

        return res[-1]


print(Solution().rob2(nums = [1,2,3,1]))
nums=[1,2,1,1]
print(Solution().rob(nums))
print(Solution().rob2(nums))








