from typing import List


class Solution:
    # O(N^2)
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:

        N = len(nums)
        res = 0
        for i, val in enumerate(nums):
            count = 1
            r = i + 1
            temp = k
            while r < N and temp >= 0:
                if nums[r] != val:
                    temp -= 1
                else:
                    count += 1
                r += 1
            res = max(res, count)

        return res

    def longestEqualSubarray2(self, nums: List[int], k: int) -> int:

        indices_x = {}
        for i, val in enumerate(nums):
            indices_x[val]=indices_x.get(val, []) + [i]


        res = 0
        for key in indices_x.keys():
            indicies = indices_x[key]
            cur_res = 1
            j = 1
            for i in range(len(indicies)):
                while j < len(indicies) and indicies[j] - indicies[i] - (j - i) <= k:
                    cur_res = max(j - i + 1, cur_res)
                    j += 1
            res = max(res, cur_res)
        return res
print(Solution().longestEqualSubarray(nums = [1,1,2,2,1,1], k = 2))
print(Solution().longestEqualSubarray(nums = [1,3,2,3,1,3], k = 3))
print(Solution().longestEqualSubarray2(nums = [1,1,2,2,1,1], k = 2))
print(Solution().longestEqualSubarray2(nums = [1,3,2,3,1,3], k = 3))


