##################################################
#
#   Aug 2020
#
##################################################
from typing import List


class Solution:
    def permuteUnique(self, nums):
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                #print("n, ans, l: ", n, ans, l)
                for i in range(len(l)+1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    print("new_ans, i: ", new_ans, i)
                    if i<len(l) and l[i]==n: break
            ans = new_ans
        return ans

##################################################
#
#   Dec 2023
#
##################################################
class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res, curr = [], []
        nums.sort()
        def backTracking(nums):
            nonlocal res, curr
            if not nums: return
            if len(nums) == 1:
                res.append(curr+nums)
                return

            i = 0
            while i < len(nums) :
                curr.append(nums[i])
                backTracking(nums[:i] + nums[i+1:])
                curr.pop()
                while i < len(nums)-1 and nums[i] == nums[i+1]:
                    i+=1
                i+=1

        backTracking(nums)
        return res

    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        N = len(nums)
        visited = [False for _ in range(N)]
        nums.sort()

        def DFS(i):
            if i >= N :
                res.append(cur.copy())

            for j in range(N):
                ############################################################################
                #
                #   Both works !!!
                #
                ############################################################################
                if j > 0 and nums[j] == nums[j-1] and visited[j-1] == False:
                #if j > 0 and nums[j] == nums[j-1] and visited[j-1] == True:
                    continue
                if not visited[j]:
                    visited[j] = True
                    cur.append(nums[j])
                    DFS(i + 1)
                    cur.pop()
                    visited[j] = False

        DFS(0)
        return res

print(Solution().permuteUnique([1,1,2]))
print(Solution2().permuteUnique([1,1,2]))