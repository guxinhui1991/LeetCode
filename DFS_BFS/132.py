from collections import defaultdict
from functools import lru_cache

class Solution:

    # Backtracking -- TLE
    def minCut0(self, s: str) -> int:
        def checkPalindrome(w):
            if not w: return False
            l, r = 0, len(w) - 1
            while l < r:
                if w[l] != w[r]: return False
                l += 1
                r -= 1
            return True


        N = len(s)
        def backTracking(idx, curr):
            nonlocal s
            if idx >= N or checkPalindrome(s[idx:N]): return 0

            for i in range(idx, N):
                if checkPalindrome(s[idx:i]):
                    curr = min(curr, 1+ backTracking(i, curr+1))

            return curr

        return backTracking(0, N-1)
    #
    # DP method
    #
    def minCut(self, s: str) -> int:
        d= defaultdict(set)
        N = len(s)
        def helper(i, j):
            while i>=0 and j<N and s[i]==s[j]:
                d[i].add(j)
                i-=1
                j+=1

        for i in range(N):
            helper(i, i)
            helper(i, i+1)

        @lru_cache(None)
        def backTracking(idx):
            if idx == N: return 0

            tmp = []
            for i in range(idx, N):
                if i in d[idx]:
                    tmp.append(backTracking(i+1)+1)
            return min(tmp)


        return backTracking(0) - 1