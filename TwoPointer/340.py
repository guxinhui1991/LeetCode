class Solution:

    # using two pointer for sliding window
    def lengthOfLongestSubstringKDistinct1(self, s: str, k: int) -> int:
        N = len(s)
        l, r = 0, 1
        res = 0

        while r <= N:
            if len(set(s[l:r])) <= k:
                res = max(res, r - l)
                r += 1
            else:
                l += 1
        return res

    # using dict for sliding window
    def lengthOfLongestSubstringKDistinct2(self, s: str, k: int) -> int:
        cur = {}
        l = 0
        N = len(s)
        res = 0
        for r in range(N):
            cur[s[r]] = cur.get(s[r], 0) + 1
            while len(cur) > k:
                cur[s[l]] -= 1
                if cur[s[l]] == 0:
                    del cur[s[l]]
                l += 1
            res = max(r - l + 1, res)

        return res


