class Solution1(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        print(text1, text2)
        m, n = len(text1), len(text2)

        if m == 0 or n == 0:
            return 0
        elif text1[-1] == text2[-1]:
            return 1 + self.longestCommonSubsequence(text1[:-1], text2[:-1])
        else:
            return max(self.longestCommonSubsequence(text1[:-1], text2), self.longestCommonSubsequence(text1, text2[:-1]))

class Solution2(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: str

        Time complexity of the above naive recursive approach is O(2^n) in worst case
        And worst case happens when all characters of X and Y mismatch i.e., length of LCS is 0.
        """
        m, n = len(text1), len(text2)

        if m == 0 or n == 0:
            return ""
        elif text1[-1] == text2[-1]:
            return self.longestCommonSubsequence(text1[:-1], text2[:-1]) + text1[-1]
        else:
            return max(self.longestCommonSubsequence(text1[:-1], text2), self.longestCommonSubsequence(text1, text2[:-1]), key=len)




class Solution3(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: str

        """
        res = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        for i in range(len(text2)):
            for j in range(len(text1)):
                print(i, j)
                res[i+1][j+1] = res[i][j] + 1 if text2[i] == text1[j] else max(res[i][j+1], res[i+1][j])

        return res[-1][-1]


    def LCS(self,text1, text2):
        if not text1 or not text2: return 0

        N1, N2 = len(text1), len(text2)
        dp = [[0 for _ in range(N1+1)] for _ in range(N2+1)]

        res = 0
        for i in range(1, N2+1):
            for j in range(1, N1+1):
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    res = max(dp[i][j], res)
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return res



print(Solution3().LCS("bsbininm", "jmjkbkjkv"))
#print(Solution1().longestCommonSubsequence("abc", "abc"))
#print(Solution1().longestCommonSubsequence("yrkzavgdmdgtqpg", "ylqpejqbalahwr"))
