class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        lo, hi = 0, 0
        N = len(s)
        for i in range(N):
            if locked[i] == 0:
                lo -= 1
                hi += 1

            else:
                if s[i] == "(":
                    lo += 1
                    hi += 1
                else:
                    lo -= 1
                    hi -= 1

            if hi < 0: return False
            if lo < 0: lo += 2

        return lo == 0

print(Solution().canBeValid(s = "))()))", locked = "010100"))
print(Solution().canBeValid(s = ")", locked = "0"))