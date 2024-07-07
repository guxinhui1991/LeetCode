class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return

        l, r = 0, len(s)-1

        while l<r:
            if(s[l].isalpha() and s[r].isalpha()):
                s = s[:l]+s[r] + s[l+1:r] + s[l]+s[r+1:]
                l+=1
                r-=1
                continue

            if(not s[l].isalpha()):
                l+=1
            if(not s[r].isalpha()):
                r-=1

        return s

s = "ab-cd"
Solution().reverseOnlyLetters(s)