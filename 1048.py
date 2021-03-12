class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dp = {}
        wordsSorted = sorted(words, key=len)
        for w in wordsSorted:
            dp[w] = max(dp.get(w[:i] + w[i+1:], 0) + 1 for i in range(len(w)))

        return max(dp.values())

print(Solution().longestStrChain(["a","b","ba","bca","bda","bdca"]))