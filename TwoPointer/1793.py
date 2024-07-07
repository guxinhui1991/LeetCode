from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        i, j = k, k
        N = len(nums)
        res = nums[k]
        cur_min = nums[k]
        while i >= 0 or j < N:
            while j < N and nums[j] >= cur_min:
                j += 1
            while i >= 0 and nums[i] >= cur_min:
                i -= 1
            res = max(res, (j - i - 1) * cur_min)
            cur_min = max(nums[i] if i >0 else 0, nums[j] if j < N else 0)
            # if i<=0 or nums[j+1] > nums[i-1]:
            #     cur_min = nums[j+1]
            #     j += 1
            # elif j >=N-1 or nums[j+1] <= nums[i-1]:
            #     cur_min = nums[i-1]
            #     i -= 1

        return res

print(Solution().maximumScore(nums = [1,4,3,7,4,5], k = 3))