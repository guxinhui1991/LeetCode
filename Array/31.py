from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        inf = float('inf')
        N = len(nums)
        ptr = N-1
        for i in range(N-1, 0, -1):
            if nums[i] > nums[i-1]:
                ptr = i -1
                break
        if ptr == N-1: return nums.reverse()

        cur_min, target, idx = inf, nums[ptr], N-1
        for i in range(N-1, ptr, -1):
            if nums[i] > target and nums[i] < cur_min:
                cur_min = nums[i]
                idx = i

        nums[ptr], nums[idx] = nums[idx], nums[ptr]
        nums[ptr+1:] = sorted(nums[ptr+1:])

        return nums




print(Solution().nextPermutation([1,3,2]))
print(Solution().nextPermutation([2,3,1]))
print(Solution().nextPermutation([1,2,3]))
print(Solution().nextPermutation([3,2,1]))



# 2019 Version
class Solution2:
    def nextPermutation(self, nums):
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i <= 0:
            nums[:] = nums[::-1]
            return

        # Find successor to pivot
        j = len(nums) - 1
        while nums[j] <= nums[i - 1]:
            j -= 1
        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        # Reverse suffix
        nums[i:] = nums[len(nums) - 1:i - 1:-1]
        # print(nums)
        return
