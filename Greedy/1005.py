class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        if all(i >= 0 for i in nums) and k % 2 == 0:
            return sum(nums)

        for i in range(k):
            if nums[i] <= 0:
                nums[i] = -nums[i]
                k -= 1
            if i == len(nums) - 1: break
        if k % 2:
            return sum(nums) - 2 * min(nums)
        else:
            return sum(nums)


