from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()


        def helper(cur, k, l_count, r_count):
            nonlocal res
            if k == 0:
                res.add("".join(cur))
                return

            if l_count < n:
                helper(cur+['('], k - 1, l_count + 1, r_count)

            if r_count < l_count:
                helper(cur+[')'], k - 1, l_count, r_count+1)

        helper([], 2*n, 0, 0)
        return res

    # TLE -
    def generateParenthesis2(self, n: int) -> List[str]:
        used = [False for _ in range(2*n)]
        cur = ["" for _ in range(2*n)]
        res = []

        def dfs(k, used, cur):
            nonlocal n, res
            if k == 0: res.append("".join(cur))

            for i in range(2*n):
                if used[i]: continue
                used[i] = True
                cur[i] = "("
                for j in range(i+1, 2*n):
                    if used[j]: continue
                    cur[j] = ")"
                    dfs(k-2, used, cur)
                    cur[j] = ""
                cur[i] = ""
            return

        dfs(2*n, used, cur)
        return res

print(Solution().generateParenthesis(3))
print(Solution().generateParenthesis2(3))
print(Solution().generateParenthesis(5))
print(Solution().generateParenthesis(6))

