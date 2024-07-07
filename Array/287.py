from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        N = len(nums) - 1
        for i in range(N + 1):
            if nums[abs(nums[i])-1] < 0 : return abs(nums[i])
            nums[abs(nums[i])-1] *= -1

        return