from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        inf = float('inf')
        N = len(nums)

        l_r, r_l = [-inf]*N, [-inf]*N
        l_min, r_min = nums[0], nums[-1]
        l_r[0], r_l[-1] = nums[0], nums[-1]
        for i in range(1, N):
            l_min = min(l_min, nums[i-1])
            l_r[i] = l_min

        for i in range(N-2, -1, -1):
            r_min = min(r_min, nums[i+1])
            r_l[i] = r_min

        res = inf
        for i in range(1, N-1):
            if l_r[i] < nums[i] and r_l[i] < nums[i]:
                res = min(res, l_r[i] + r_l[i] + nums[i])

        return -1 if res==inf else res


# using monotonic stack
class Solution2:
    def minimumSum(self, nums: List[int]) -> int:
        inf = float('inf')
        N = len(nums)

        def getPeak(arr):
            nonlocal N
            l = [-1] * N

            stack = []
            for i in range(N):
                while stack and arr[i] <= arr[stack[-1]]:
                    stack.pop()
                l[i] = -1 if not stack else stack[0]
                stack.append(i)

            return l

        l = getPeak(nums)
        r = getPeak(nums[::-1])[::-1]


        res = inf
        for i in range(1, N-1):
            if l[i] != -1 and r[i] != -1:
                res = min(res, nums[l[i]] + nums[::-1][r[i]] + nums[i])

        return -1 if res==inf else res




Solution().minimumSum(nums = [5,4,8,7,10,2])
Solution().minimumSum(nums = [5,5,5])
Solution().minimumSum(nums = [8,6,1,5,3])
