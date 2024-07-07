from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_dic = Counter(t)
        t_chars = len(t_dic)

        res = [0, 0]
        matched, res_len = 0, sys.maxsize

        N = len(s)
        cur_dic = {}
        l, r = 0, 0

        while r < N:
            cur_dic[s[r]] = cur_dic.get(s[r], 0) + 1
            if s[r] in t_dic and cur_dic[s[r]] == t_dic[s[r]]:
                matched += 1

            while l<=r and matched == t_chars:

                if r - l + 1< res_len:
                    res_len = r-l+1
                    res = [l, r+1]
                cur_dic[s[l]] -= 1
                if s[l] in t_dic and cur_dic[s[l]] < t_dic[s[l]]: matched -=1
                l += 1
            r += 1

        return s[res[0]:res[1]]