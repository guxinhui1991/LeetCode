from collections import Counter
from typing import List


class Solution:
    #
    #   Using array
    #
    def findAnagrams(self, s: str, p: str) -> List[int]:
        N = len(s)
        k = len(p)
        cur_dic = {}
        if N < k: return []

        target = [0] * 26
        cur_count = [0] * 26
        for i in range(k):
            target[ord(p[i]) - ord('a')] += 1
            cur_count[ord(s[i]) - ord('a')] += 1

        res = []
        l, r = 0, k
        if tuple(cur_count) == tuple(target): res.append(0)

        for i in range(1, N - k + 1):
            cur_count[ord(s[l]) - ord('a')] -= 1
            cur_count[ord(s[r]) - ord('a')] += 1
            if tuple(cur_count) == tuple(target): res.append(i)
            l += 1
            r += 1

        return res


    #
    #   Using dictionary
    #
    def findAnagrams2(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        dp = Counter(p)

        ds = {}
        res = []
        for i in range(ns):
            ds[s[i]] = ds.get(s[i], 0) + 1

            if i >= np:
                if ds[s[i - np]] == 1:
                    del ds[s[i - np]]
                else:
                    ds[s[i - np]] -= 1

            if ds == dp:
                res.append(i - np + 1)

        return res


Solution().findAnagrams2("cbaebabacd", "abc")