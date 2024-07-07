class Solution(object):
    def strStr(self, pat, txt):
        N = len(txt)
        M = len(pat)
        lps = self.buildLPSArray(pat, M)

        i, j = 0, 0

        res_idx = []
        while i < N:
            if txt[i] == pat[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                    continue
                else:
                    j = lps[j-1]

            if j == M:
                res_idx.append(i-j)
                j = lps[j-1]

        return res_idx
    def buildLPSArray(self, pat, M):

        lps = [0 for _ in range(M)]
        i = 1
        cur_len = 0 # length of prefix == suffix
        while i < M :
            if pat[i] == pat[cur_len]:
                lps[i] = cur_len + 1
                cur_len += 1
                i += 1
            else:
                lps[i] = 0
                i += 1
                if cur_len > 0 : cur_len = lps[cur_len-1] # Important

        return lps


class Solution2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        N = len(haystack)
        M = len(needle)

        lps = [0] * M

        cur_len, i = 0, 1
        while i < M:
            if needle[i] == needle[cur_len]:
                cur_len += 1
                lps[i] = cur_len
                i+=1
            else:
                if cur_len != 0:
                    cur_len = lps[cur_len-1]
                else:
                    lps[i] = 0
                    i+=1


        i, j = 0, 0
        while i < N:
            if haystack[i] == needle[j]:
                j += 1
                i += 1

            else:
                if j == 0:
                    i+=1
                    continue
                else:
                    j = lps[j-1]

            if j == M:
                return i - M

        return -1


print(Solution2().strStr("aabaaabaaac", "aabaaac"))
print(Solution2().strStr("sadbutsad", "sad"))
