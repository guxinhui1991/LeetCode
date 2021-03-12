class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        numMax = nums[0]
        numMaxIdx = 0
        for i in range(1, len(nums)):
            if nums[i] > numMax:
                numMax = nums[i]
                numMaxIdx = i

        if k == 1: return numMax
        else : return self.findKthLargest(nums[:numMaxIdx] + nums[numMaxIdx+1:], k-1)

    def findKthLargest1(self, nums, k):
        sortedNums = sorted(nums)
        return sortedNums[len(nums)-k]
import time
start_time = time.time()
print(Solution().findKthLargest([3,2,1,5,6,4], 2))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(Solution().findKthLargest1([3,2,1,5,6,4], 2))
print("--- %s seconds ---" % (time.time() - start_time))
