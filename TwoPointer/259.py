class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        res = 0
        for i, val in enumerate(nums):
            t_temp = target - val

            l, r = i + 1, N - 1

            while l < r:
                if nums[l] + nums[r] < t_temp:
                    res += r - l
                    l += 1
                else:
                    r -= 1

        return res

