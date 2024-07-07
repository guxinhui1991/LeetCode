from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        dict_res = {0:1}
        cur_sum, res = 0, 0
        for i, val in enumerate(nums):
            cur_sum += nums[i]
            res += dict_res.get(cur_sum - k, 0)
            dict_res[cur_sum] = dict_res.get(cur_sum, 0) + 1
        return res




print(Solution().subarraySum([1,1,1], 2))
print(Solution().subarraySum([1], 0))