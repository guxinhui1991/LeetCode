from typing import List


class Solution:

    # O(N) Time
    # O(N) Space
    def findDisappearedNumbers1(self, nums: List[int]) -> List[int]:
        cur = set(nums)
        N = len(nums)
        all = set([i for i in range(1, N + 1)])

        return all ^ cur

    # O(N) Time
    # O(1) Space
    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:

        N = len(nums)

        res = []
        for i in range(N):
            idx = abs(nums[i]) - 1
            nums[idx] = -abs(nums[idx])
        for i in range(N):
            if nums[i] > 0: res.append(i+1)
        return res
