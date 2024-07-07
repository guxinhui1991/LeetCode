from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res, cur = set(), []
        N = len(nums)

        def DFS(i):
            if len(cur) > 1: res.add(tuple(cur.copy()))
            for j in range(i, N):
                if not cur or nums[j] >= cur[-1]:
                    cur.append(nums[j])
                    DFS(j + 1)
                    cur.pop()

        DFS(0)
        return res
    def findSubsequences2(self, nums: List[int]) -> List[List[int]]:
        res, curr = set(), []

        def dfs(nums_in):
            if not nums: return
            for i,val in enumerate(nums_in):
                if not curr or val >= curr[-1]:
                    curr.append(val)
                    dfs(nums_in[i+1:])
                    if(len(curr)>1 and tuple(curr) not in res): res.add(tuple(curr.copy()))
                    curr.pop()
                    while i<len(nums_in)-1 and nums_in[i]==nums_in[i+1]:
                        i+=1

            return

        dfs(nums)
        return list(res)


import timeit

start = timeit.default_timer()
print(Solution().findSubsequences([4,6,7,7]))
print(Solution().findSubsequences([4,4,3,2,1]))
stop = timeit.default_timer()
print('Time: ', stop - start)


start = timeit.default_timer()
print(Solution().findSubsequences2([4,6,7,7]))
print(Solution().findSubsequences2([4,4,3,2,1]))
stop = timeit.default_timer()
print('Time: ', stop - start)
