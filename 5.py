class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        if(len(s) <= 1): return s;

        start, end = 0, 0
        for i in range(len(s)):
            res1 = self.expandFromMiddle(s, i, i)
            res2 = self.expandFromMiddle(s, i, i + 1)

            tempRes = max(res1, res2)
            if(tempRes > (end - start + 1)):
                start = i - int((tempRes-1)/2)
                end = i + int(tempRes/2)
            res = s[start:end+1]
        return res


    def expandFromMiddle(self, s, start, end):
        if (start > end): return 0

        while ((start >= 0) and (end < len(s)) and (s[start] == s[end])):
            start = start - 1
            end = end + 1

        return end - start - 1


if __name__ == '__main__':
    print(Solution().longestPalindrome('cbbd'))
    print(Solution().longestPalindrome('abcba'))
    print(Solution().longestPalindrome('ababd'))
