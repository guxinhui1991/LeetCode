from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        N = len(temperatures)
        stack = []
        res = [0 for _ in range(N)]

        for i in range(N):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                cur_i = stack.pop()
                res[cur_i] = i - cur_i

            stack.append(i)
            #cur_val = [temperatures[i] for i in stack]

        return res

print(Solution().dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))
