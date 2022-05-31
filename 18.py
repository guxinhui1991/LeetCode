class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i == 0 or nums[i] != nums[i - 1]:
                comb3 = self.threeSum(nums[i+1:], -nums[i])
                for c in comb3:
                    res.append(sorted([nums[i]] + list(c)))

        return res

    def threeSum(self, nums, targetIn):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1] : continue
            target = targetIn - nums[i]
            l, r = i+1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    l = l + 1
                    r = r - 1
                elif nums[l] + nums[r] < target:
                    l = l + 1
                else:
                    r = r - 1
        return res

print(Solution().fourSum([1,0,-1,0,-2,2], 0))
