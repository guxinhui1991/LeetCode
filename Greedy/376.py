from typing import List


class Solution(object):
    def wiggleMaxLength(self, nums):
        N = len(nums)

        res = 1
        prev = 0
        for i in range(1, N):
            cur = nums[i] - nums[i-1]
            if prev * cur <= 0 and cur:
                prev = cur
                res += 1
        return res

class Solution_DP:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        # max length up to i, w. last index up-slope
        dp_up = [0 for _ in range(len(nums))]
        # max length up to i, w. last index down-slope
        dp_down = [0 for _ in range(len(nums))]

        dp_up[0], dp_down[0] = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp_up[i] = dp_down[i-1] + 1
                dp_down[i] = dp_down[i-1]
            elif nums[i] < nums[i-1]:
                dp_down[i] = dp_up[i-1] + 1
                dp_up[i] = dp_up[i-1]
            else:
                dp_up[i] = dp_up[i-1]
                dp_down[i] = dp_down[i - 1]

        return max(dp_down[-1], dp_up[-1])



nums=[0,0]
print(Solution().wiggleMaxLength(nums))
print(Solution_DP().wiggleMaxLength(nums))
print('-----------------------------------')
nums=[0,0,0]
print(Solution().wiggleMaxLength(nums))
print(Solution_DP().wiggleMaxLength(nums))
print('-----------------------------------')
nums=[1,7,4,9,2,5]
print(Solution().wiggleMaxLength(nums))
print(Solution_DP().wiggleMaxLength(nums))
print('-----------------------------------')
nums=[1,17,5,10,13,15,10,5,16,8]
print(Solution().wiggleMaxLength(nums))
print(Solution_DP().wiggleMaxLength(nums))
print('-----------------------------------')
