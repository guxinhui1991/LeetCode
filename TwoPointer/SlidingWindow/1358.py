class Solution:
    def numberOfSubstrings1(self, s: str) -> int:

        N = len(s)
        count_a, count_b, count_c = 0, 0, 0
        res = 0
        r = 0
        for i in range(N):
            while r < N and not (count_a and count_b and count_c):
                if s[r] == "a":
                    count_a += 1
                elif s[r] == "b":
                    count_b += 1
                elif s[r] == "c":
                    count_c += 1
                r += 1

            if (count_a and count_b and count_c):
                res += N - r + 1

            if s[i] == "a":
                count_a -= 1
            elif s[i] == "b":
                count_b -= 1
            elif s[i] == "c":
                count_c -= 1


        return res

    #
    # Simplified Solution 2 and 3
    #
    def numberOfSubstrings2(self, s: str) -> int:
        l = 0
        N = len(s)
        cur = {c: 0 for c in "abc"}
        res = 0
        for r in range(N):
            cur[s[r]] += 1
            while all(cur.values()):
                res += N - r
                cur[s[l]] -= 1
                l += 1

        return res

    def numberOfSubstrings3(self, s: str) -> int:
        l = 0
        N = len(s)
        cur = {c: 0 for c in "abc"}
        res = 0
        for r in range(N):
            cur[s[r]] += 1

            while all(cur.values()):
                cur[s[l]] -= 1
                l += 1
            res += l

        return res
s = "abcabc"
print(Solution().numberOfSubstrings(s))
