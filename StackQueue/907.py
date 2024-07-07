from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        inf = float('inf')
        arr = [-inf] + arr + [-inf]
        stack = []
        MOD = 10 ** 9 + 7
        res = 0
        for i, val in enumerate(arr):
            while stack and val < arr[stack[-1]]:
                m = stack.pop()
                prev = stack[-1]
                res += (m - prev) * (i - m) * arr[m]

            stack.append(i)
        # res += sum([arr[i] * 2 **(stack[-1] - i) for i in stack])
        return res % MOD


Solution().sumSubarrayMins([3,1,2,4])