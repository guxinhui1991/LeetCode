from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, curr = [], []
        candidates.sort()
        def helper(nums, t):
            nonlocal res, curr
            if t < 0:
                return
            if t == 0:
                res.append(curr.copy())
            i = 0
            while i<len(nums):
                curr.append(nums[i])
                helper(nums[i+1:], t-nums[i])
                curr.pop()
                while(i<len(nums) and nums[i-1] == nums[i]):
                    i+=1
                i+=1
        helper(candidates, target)
        return [list(x) for x in set(tuple(sorted(x)) for x in res)]


    # Mar 2024
    # change function signature for current , easier to read
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(arr, t, cur):
            nonlocal res
            if t < 0: return
            if t == 0: res.append(cur)

            for i, v in enumerate(arr):
                if (i>0 and arr[i]==arr[i-1]): continue
                dfs(arr[i+1:], t-v, cur+[v])
            return

        dfs(candidates, target, [])
        return res


candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
print(Solution().combinationSum2(candidates,30))
print(Solution().combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))