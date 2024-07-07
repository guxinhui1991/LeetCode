from typing import List


class Solution:

    # O(N)
    def findMin1(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        return nums[0]
    # Binary search
    def findMin2(self, nums: List[int]) -> int:
        N = len(nums)
        l, r = 0, N - 1

        while l < r:
            m = l + (r-l)//2
            if nums[m] > nums[m+1]:
                return nums[m+1]

            if nums[m] > nums[l] and nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

        return nums[r]

Solution().findMin2([11,13,15,17])