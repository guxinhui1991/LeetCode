class Solution:
    def myPow(self, x: float, n: int) -> float:
        def binaryExp(x, n):
            if n == 0: return 1

            if n < 0:
                return binaryExp(1 / x, -n)

            res = 1
            while n != 0:
                if n % 2:
                    res *= x
                    n = n - 1
                else:
                    x *= x
                    n = n // 2

            return res

        return binaryExp(x, n)


print(Solution().myPow(2, 10))
print(Solution().myPow(2, -2))