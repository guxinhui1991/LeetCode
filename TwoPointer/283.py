from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return

        N = len(nums)
        s, f = 0, 0

        while s< N and f < N:
            if nums[s] == 0:
                while f < N and nums[f] == 0:
                    f += 1
                if f >= N: break
                nums[s] = nums[f]
                nums[f] = 0
            s += 1
            f += 1

        return nums