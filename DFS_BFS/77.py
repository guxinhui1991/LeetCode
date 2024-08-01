from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]
        def generateCombine(nums, k):
            if k == 0: return []
            if k == 1: return [[i] for i in nums]
            cur_len = len(nums)
            res = []

            if cur_len < k: return []
            if cur_len == k: return [nums]

            for i in range(cur_len):
                cur_res = generateCombine(nums[i + 1:], k - 1)
                res = res + [[nums[i]] + item for item in cur_res]
            return res

        return generateCombine(nums, k)

    def combine_backtracking(self, n, k):
        self.res, self.path = [], []
        nums_in = [i + 1 for i in range(n)]

        def back_tracking(nums, k):
            if len(self.path) == k:
                self.res.append(self.path.copy())
                return
            for i, val in enumerate(nums):
                self.path.append(val)
                back_tracking(nums[i+1:], k)
                self.path.pop()

        back_tracking(nums_in, k)
        return self.res


    # Jul 2024
    #
    #   Cutting of unnecessary loops.
    #   e.g, n = 4, k = 4. Loop for [2, 3, 4] will not return possible candidates.
    #
    def combine_backtracking_optimized(self, n, k):
        res, path = [], []
        nums = [i + 1 for i in range(n)]

        def back_tracking(idx_start):
            nonlocal nums, path, n, k
            if len(path) == k:
                res.append(path.copy())
                return
            for i in range(idx_start, n - (k-len(path)) + 1):
                path.append(nums[i])
                back_tracking(i+1)
                path.pop()

        back_tracking(0)
        return res


import timeit

start = timeit.default_timer()
Solution().combine(40, 6)
stop = timeit.default_timer()
print('Time: ', stop - start)

start = timeit.default_timer()
Solution().combine_backtracking(40, 6)
stop = timeit.default_timer()
print('Time: ', stop - start)