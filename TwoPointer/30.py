from typing import List
from collections import Counter


class Solution:

    # Memory Limit Exceeded
    def findSubstring1(self, s: str, words: List[str]) -> List[int]:
        len_w = len(words[0]) * len(words)
        p = set()
        cur = []

        def backTracking(w):
            nonlocal cur
            if not w:
                p.add("".join(cur))
                return
            for i in range(len(w)):
                cur.append(w[i])
                backTracking(w[:i] + w[i + 1:])
                cur.pop()

        backTracking(words)

        res = []
        for i in range(len(s)):
            if (s[i:i + len_w]) in p:
                res.append(i)

        return res


    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        len_w = len(words[0])
        len_all = len(words)
        len_p = len_w * len_all
        word_dic = Counter(words)

        def check(i):
            w_dic = word_dic.copy()
            count = 0
            for j in range(i, i + len_p, len_w):
                cur = s[j: j+len_w]
                if w_dic[cur] > 0:
                    w_dic[cur] -= 1
                    count += 1
                else:
                    break
            return count == len_all

        res = []
        for i in range(0, len(s) - len_p + 1):
            if check(i):
                res.append(i)


        return res


print(Solution().findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))
print(Solution().findSubstring1(s = "barfoothefoobarman", words = ["foo","bar"]))