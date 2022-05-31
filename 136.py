class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if (len(s.replace(" ", "")) == 0) or (s in wordDict):
            return True

        elif len(s.replace(" ", "")) <= 0:
            return False

        else:
            res = False
            for w in wordDict:
                if w in s:
                    if self.wordBreak(s.replace(w, " "*len(w)), wordDict):
                        return True
                else:
                    continue
            return False

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(Solution().wordBreak(s, wordDict))