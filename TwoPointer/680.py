class Solution:
    def validPalindrome(self, s: str) -> bool:

        def checkPalindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]: return False
                l += 1
                r -= 1
            return True

        N = len(s)
        l, r = 0, N - 1
        count = 0
        while r - l > 1:

            if s[l] != s[r]:
                return checkPalindrome(s[l:r]) or checkPalindrome(s[l + 1:r + 1])
            r -= 1
            l += 1

        return True
print(Solution().validPalindrome("ebcbbececabbacecbbcbe"))