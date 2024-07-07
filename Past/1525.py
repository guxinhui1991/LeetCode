class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """

        numChars = len(s)
        resF = [1] * numChars
        resB = [1] * numChars
        freqF = {s[0] : 1}
        freqB = {s[-1] : 1}

        for i in range(1, numChars):
            if s[i] in freqF.keys():
                freqF[s[i]] = freqF[s[i]]+1
                resF[i] = resF[i - 1]
            else:
                freqF[s[i]] = 1
                resF[i] = resF[i - 1] + 1

            idx = numChars - i - 1
            if s[idx] in freqB.keys():
                freqB[s[idx]] = freqB[s[idx]] + 1
                resB[idx] = resB[idx + 1]
            else:
                freqB[s[idx]] = 1
                resB[idx] = resB[idx + 1] + 1

        res = 0
        for i in range(numChars-1):
            if resF[i] == resB[i+1] :
               res = res + 1

        return res


print(Solution().numSplits("abcd"))
print(Solution().numSplits("aaaaa"))
print(Solution().numSplits("acbadbaada"))