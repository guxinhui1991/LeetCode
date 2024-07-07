class Solution(object):
    # Apr 2023
    def twoSum(self, nums, target):
        nums = sorted(enumerate(nums), key=lambda i: i[1])

        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l][1] + nums[r][1] == target:
                return [nums[l][0], nums[r][0]]
            elif nums[l][1] + nums[r][1] < target:
                l += 1
            elif nums[l][1] + nums[r][1] > target:
                r -= 1

        return []

    # Dec 2023
    def twoSum2(self, nums, target):
        map_res = {}

        for i, n in enumerate(nums):
            if target - n in map_res:
                return [map_res[target - n],i]
            else:
                map_res[n] = i
        return

