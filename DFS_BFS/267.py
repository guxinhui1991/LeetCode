from collections import Counter
from typing import List


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        def check(w):
            l, r = 0, len(w) - 1
            while l < r:
                if w[l] != w[r]: return False
                l += 1
                r -= 1
            return True

        N = len(s)
        s = sorted(list(s))
        cur_dic = Counter(s)
        cur = [0 for _ in range(N)]
        res = []


        def dfs(i):
            if i >= N//2 and check(cur):
                if all(v==0 for _,v in cur_dic.items()):
                    res.append("".join(cur))
                else:
                    cur[N//2] = next(k for k, v in cur_dic.items() if v > 0)
                    res.append("".join(cur))
                return
            elif i == N-1 :
                res.append("".join(cur))
                return

            for k,v in cur_dic.items():
                if v>=2:
                    cur[i] = k
                    cur[-(i+1)] = k
                    cur_dic[k] -= 2
                    dfs(i + 1)
                    cur[i] = 0
                    cur[-(i+1)] = 0
                    cur_dic[k] += 2

        if len([v for v in cur_dic.values() if v%2])>1:
            return []

        dfs(0)
        return res

print(Solution().generatePalindromes("aabb"))
print(Solution().generatePalindromes("aabbc"))