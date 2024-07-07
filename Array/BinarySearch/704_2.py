class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high= 0, len(nums) -1
        mid = (low + high )//2

        while (high >= low):
            mid = low + (high - low) // 2
            if (nums[mid] == target): return mid

            if (nums[mid] < target): low = mid + 1
            elif (nums[mid] > target): high = mid - 1

        return -1



print(Solution().search(nums = [-1,0,3,5,9,12], target = 13))