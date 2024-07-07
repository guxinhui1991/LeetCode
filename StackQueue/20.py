class Solution(object):
    ##############################################
    #   Aug 2020
    ##############################################

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        charDic = {"(": ")", "{": "}", "[": "]"}

        if (not s): return True
        if (len(s) % 2 > 0): return False

        tempC = []
        for i in range(len(s)):
            if s[i] in list(charDic.keys()):
                tempC.append(s[i])
            elif (len(tempC) == 0):
                return False
            elif (s[i] != charDic[tempC.pop()]):
                return False

        if len(tempC) > 0: return False

        return True

##############################################
#   Dec 2023
##############################################
class Solution2:
    def isValid(self, s: str) -> bool:
        if len(s) % 2: return False

        stack = []
        dic = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        for c in s:
            if c in dic:
                if not stack or dic[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return True if not stack else False
print(Solution2().isValid(s = "()[]{}"))