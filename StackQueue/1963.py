class Solution:
    def minSwaps(self, s: str) -> int:
        count = 0
        res = 0
        l = 0 # count the number of "[" until current step
        N = len(s)
        for i in s:
            if i == "[":
                l += 1
                if l> N//2: break
                count += 1
            else:
                count -= 1

            if count < 0:
                count = 1
                l += 1
                res += 1

        return res

    # Mar 2024
    # Optimized since we only need to count the number of open brackets
    def minSwaps2(self, s: str) -> int:
        res, d = 0, 0
        for i in s:
            if i=="[":
                d += 1
            else:
                if d==0:
                    res += 1
                    d += 1
                else:
                    d -= 1
        return res

print(Solution().minSwaps(s = "][]["))
print(Solution().minSwaps2(s = "][]["))