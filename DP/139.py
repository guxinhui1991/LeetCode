from typing import List


class Solution:
    # Dec 2023 -- Dynamic programming
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        N = len(s)
        dp = [0 for _ in range(N+1)]

        dp[0] = True
        for i,val in enumerate(range(N+1)):
            for j in range(i):
                cur_word = s[j: i]
                if cur_word in wordDict and dp[j] == True:
                    dp[i] = True

        return dp[-1]


print(Solution().wordBreak(s = "leetcode", wordDict = ["leet","code"]))