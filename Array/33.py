class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        shift = 0
        for i in range(1, len(nums)):
            if(nums[i] < nums[i-1]):
                shift = i
                break
        arr = [0] * len(nums)
        for j in range(len(nums)):
            arr[j] = nums[(shift +j)%len(nums)]


        for i in range(len(arr)):
            if(arr[i] == target): return (i+shift)%len(arr)
            if(arr[i] > target): return -1


print(Solution().search(nums = [3, 1], target = 3))