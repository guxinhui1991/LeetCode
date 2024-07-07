from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res, path = [], []
        nums = [i+1 for i in range(9)]

        def generateRes(nums, k, n):
            nonlocal res
            if len(path) >= k:
                if sum(path) == n: res.append(path.copy())
                return

            for i, val in enumerate(nums):
                path.append(val)
                generateRes(nums[i+1:], k, n)
                path.pop()

        generateRes(nums, k, n)

        return res

Solution().combinationSum3(3, 7)