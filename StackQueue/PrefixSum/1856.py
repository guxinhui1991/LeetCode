from typing import List


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:

        N = len(nums)
        cur_sum = [0 for _ in range(N + 1)]

        for i in range(1, N+1):
            cur_sum[i] = nums[i-1] + cur_sum[i-1]

        stack = []
        nums = nums
        res = 0
        for i in range(N+1):
            while stack and (i==N or nums[i] < nums[stack[-1]]):
                cur = stack.pop()
                res = max(res, nums[cur] * (cur_sum[i] - cur_sum[1 + stack[-1] if stack else 0]))
            stack.append(i)

        return res % (10**9 + 7)


print(Solution().maxSumMinProduct([1,2,3,2]))
print(Solution().maxSumMinProduct([2,3,3,1,2]))
print(Solution().maxSumMinProduct([3,1,5,6,4,2]))