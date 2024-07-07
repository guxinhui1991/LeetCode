from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, curr = [[]], []
        nums.sort()
        def dfs(nums):
            if not nums:
                return

            for i in range(len(nums)):
                curr.append(nums[i])
                dfs(nums[i + 1:])
                res.append(curr.copy())
                curr.pop()
                while 0<i<len(nums) and nums[i]==nums[i-1]:
                    i+=1
                    continue
            return

        dfs(nums)
        def func(x):
            if x: return x[0], len(x)
            else: return 0, 0

        return sorted(list(set(tuple(i) for i in res)), key=func)


    def subsetsWithDup1(self, nums: List[int]) -> List[List[int]]:
        res = set()
        cur = []
        N = len(nums)
        def backTracking(i):
            res.add(tuple(cur))
            for j in range(i, N):
                cur.append(nums[j])
                backTracking(j + 1)
                cur.pop()
            return

        nums.sort()
        backTracking(0)
        return [list(i) for i in res]

print(Solution().subsetsWithDup([1,2,2]))