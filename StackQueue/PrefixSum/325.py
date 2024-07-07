from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        cum_sum = [0 for _ in range(len(nums) + 1)]
        cur_dic = {0:[0]}
        for i in range(1, len(nums)+1):
            cur_val = cum_sum[i - 1] + nums[i - 1]
            cur_dic[cur_val] = cur_dic.get(cur_val, []) + [i]
            cum_sum[i] = cur_val

        cur_max = 0
        for i in range(len(nums)):
            if (cum_sum[i+1]-k) in cur_dic:
                cur_max = max(cur_max, i + 1 - cur_dic[cum_sum[i+1] - k][0])

        return cur_max

    # Optimzed - no need to keep list of index in dict
    def maxSubArrayLen2(self, nums: List[int], k: int) -> int:
        d = {0:-1}
        res = cur = 0

        for i, v in enumerate(nums):
            cur += v
            if cur - k in d:
                res = max(i - d[cur - k], res)
            if cur not in d:
                d[cur] = i
        return res

print(Solution().maxSubArrayLen([1,-1,5,-2,3], 3))
print(Solution().maxSubArrayLen2([1,-1,5,-2,3], 3))