from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        res_first = [0 for _ in range(len(nums)+1)]
        res_first[0], res_first[1] = 0, nums[0]
        for i in range(2, len(nums)):
            res_first[i] = max(nums[i-1] + res_first[i-2], res_first[i - 1])
        res_first[len(nums)] = res_first[len(nums) - 1]

        res_zero = [0 for _ in range(len(nums) + 1)]
        res_zero[0], res_zero[1] = 0, 0
        for i in range(2, len(nums)+1):
            res_zero[i] = max(nums[i-1] + res_zero[i-2], res_zero[i - 1])

        return max(res_first[-1], res_zero[-1])

print(Solution().rob(nums = [2,3,2]))
print(Solution().rob(nums = [1,2,3,1]))