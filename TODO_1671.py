class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        lenNums = len(nums)
        maxNums = nums[0]
        maxIdx = 0
        for i in range(1, lenNums):
            if(nums[i] > maxNums):
                maxNums = nums[i]
                maxIdx = i

        idxUp = []
        idxDown = []
        for i in range(lenNums - 1):
            if(nums[i] >= nums[i-1]):
                idxUp.append(i)
            if(nums[lenNums - i - 1] > nums[lenNums - i - 2])
