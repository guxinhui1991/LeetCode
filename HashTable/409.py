
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for i, c in enumerate(s):
            count[c] = count.get(c, 0) + 1

        flag = 0
        res = 0
        for k, v in count.items():
            if v % 2 == 0:
                res += v
            else:
                res += v - 1
                flag = 1

        return res + flag

s = "abccccdd"

print(Solution().longestPalindrome(s))
