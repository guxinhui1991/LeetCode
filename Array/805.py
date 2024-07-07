class Solution(object):
    def splitArraySameAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if(len(nums) == 1): return False
        if(len(nums) == 2): return nums[0] == nums[1]

        target = sum(nums) / len(nums)



