from typing import List

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        N, res = len(nums), 0
        inf = float('inf')
        vals = [-inf] + nums + [-inf]
        stack = []
        for i,val in enumerate(vals):
            while stack and val < vals[stack[-1]]:
                cur = stack.pop()
                prev = stack[-1]
                res -= vals[cur] *(i - cur) * (cur - prev)
            stack.append(i)

        vals = [inf] + nums + [inf]
        stack = []
        for i,val in enumerate(vals):
            while stack and val > vals[stack[-1]]:
                cur = stack.pop()
                prev = stack[-1]
                res += vals[cur] *(i - cur) * (cur - prev)
            stack.append(i)

        return res

Solution().subArrayRanges([4,-2,-3,4,1]
)