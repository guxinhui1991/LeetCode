from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0 for _ in range(n)]
        stack = []
        prev = 0
        for s in logs:
            t, arr, t1 = s.split(":")
            t, t1 = int(t), int(t1)

            if arr == "start":
                if stack: res[stack[-1]] += t1 - prev
                stack.append(t)
                prev = t1
            else:
                stack.pop()
                res[t] += t1 - prev + 1
                prev = t1 + 1
        return res

print(Solution().exclusiveTime(n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]))