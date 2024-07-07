from typing import List


class Solution:


    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(s):
            return s == s[::-1]

        curr = []
        def dfs(s):
            if not s: return
            if isPalindrome(s):
                res.append(curr+[s])

            for i, c in enumerate(s):
                if isPalindrome(s[:i+1]):
                    curr.append(s[:i+1])
                    dfs(s[i+1:])
                    curr.pop()
                else:
                    continue
            return

        dfs(s)
        return res


    def partition1(self, s: str) -> List[List[str]]:
        res, curr = [], []
        N = len(s)

        def checkPalindrome(w):
            if w == "": return False
            l, r = 0, len(w) - 1
            while l < r:
                if w[l] != w[r]: return False
                l += 1
                r -= 1
            return True

        def backTracking(idx):
            nonlocal res, curr
            if idx >= N:
                res.append(curr.copy())
                return

            for i in range(idx, N+1):
                if checkPalindrome(s[idx: i]):
                    curr.append(s[idx:i])
                    backTracking(i)
                    curr.pop()
            return



print(Solution().partition("bb"))
print(Solution().partition("abab"))
print(Solution().partition("aab"))