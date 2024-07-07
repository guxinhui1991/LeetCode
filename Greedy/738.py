class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        n_str = list(str(n))

        ptr, flag = len(n_str) -1, len(n_str)
        while ptr > 0:
            if n_str[ptr] < n_str[ptr - 1]:
                # n_str[ptr] = "9"
                n_str[ptr - 1] = str(int(n_str[ptr - 1]) - 1)
                flag = ptr
            ptr -= 1

        n_str[flag:len(n_str)] = ["9" for _ in n_str[flag:len(n_str)]]
        return int("".join(n_str))



print(Solution().monotoneIncreasingDigits(10))
print(Solution().monotoneIncreasingDigits(332))
print(Solution().monotoneIncreasingDigits(1234))
print(Solution().monotoneIncreasingDigits(989998))