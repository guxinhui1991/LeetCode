from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        inf = float('inf')
        nums = [-inf] + nums + [-inf]
        N = len(nums)
        l, r = 1, N

        while l <= r:
            m = (l + r)//2

            if nums[m]>nums[m-1] and nums[m]>nums[m+1]: return m - 1
            elif nums[m] < nums[m-1]: r=m-1
            elif nums[m] < nums[m+1]: l=m+1

        return l - 1


print(Solution().findPeakElement([1,2]))
print(Solution().findPeakElement([1,2,1,3,5,6,4]))
print(Solution().findPeakElement([1,2,3,1]))