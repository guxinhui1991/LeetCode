from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        cur_m = 1
        cur_n = 1
        max_p = float('-inf')

        for n in nums:
            tmp_m = cur_m*n
            tmp_n = cur_n*n

            cur_m = max(tmp_m, n, tmp_n)
            cur_n = min(tmp_m, n, tmp_n)
            max_p = max(max_p, cur_m)

        return max_p


print(Solution().maxProduct([-2, -3, -4]))
print(Solution().maxProduct([-2, 3, -4]))
print(Solution().maxProduct([-2, 0, -1]))