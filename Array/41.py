from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        N = len(nums)

        for i in range(N):
            while 0 < nums[i] <= N and nums[i]!= i+1 and nums[nums[i] - 1] != nums[i]:
                tmp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = tmp

        for i in range(N):
            if nums[i] != i + 1: return i + 1

        return N + 1

    def firstMissingPositive2(self, nums: List[int]) -> int:
        nums.insert(0, 0)
        N = len(nums)

        for i in range(N):
            if nums[i] < 0 or nums[i] >= N: nums[i] = 0

        for i in range(N):
            if nums[i] > 0:
                idx = nums[i]%N - 1
                nums[idx] += N

        for i in range(N):
            if nums[i] // N == 0: return i + 1

        return N + 1



print(Solution().firstMissingPositive2([3, 1]))
print(Solution().firstMissingPositive2([3, 4, -1, 1]))