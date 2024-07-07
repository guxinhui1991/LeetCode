from typing import List


class Solution:
    #########################################################
    # Aug 2018
    #########################################################
    def search_path(self, candidates, target, index, cur_path, res):
        if target == 0:
            res.append(cur_path)
            print('Yes')
            return

        if target < candidates[0]:
            return

        for i in range(index, len(candidates)):
            target_new = target - candidates[i]
            self.search_path(candidates, target_new, i, cur_path + [candidates[i]], res)

    def combinationSum0(self, candidates, target):
        res = []
        candidates = sorted(candidates)
        self.search_path(candidates, target, 0, [], res)
        return res

    #########################################################
    #
    # Dec 2023
    #
    #########################################################
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, path = [], []

        def backTracking(arr_in, t):
            nonlocal res, path
            if t < 0: return
            if t == 0:
                res.append(path.copy())
                return

            for i, val in enumerate(arr_in):
                path.append(val)
                backTracking(arr_in[i:], t - val)
                path.pop()

        backTracking(candidates, target)
        return [list(x) for x in set(tuple(sorted(x)) for x in res)]


print(Solution().combinationSum([2, 3, 6, 7], 8))
