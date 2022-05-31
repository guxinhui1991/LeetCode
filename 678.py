class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        cMax, cMin = 0, 0
        for c in s:
            if c == '(':
                cMax = cMax + 1
                cMin = cMin + 1
            elif c == ')':
                cMax = cMax - 1
                cMin = cMin - 1
            elif c == '*':
                cMax = cMax + 1
                cMin = cMin - 1

            if cMax < 0: return False
            cMin = max(cMin, 0)
        return cMax * cMin <= 0

print(Solution().checkValidString("(*)"))
print(Solution().checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
print(Solution().checkValidString("()"))