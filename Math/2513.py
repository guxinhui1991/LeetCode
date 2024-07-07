class Solution:
    def minimizeSet(self, d1: int, d2: int, C1: int, C2: int) -> int:
        def lcm(x, y):
            return x * y // math.gcd(x, y)

        def check(x):
            l1 = (x - x//d1) >= C1
            l2 = (x - x//d2) >= C2
            l3 = (x - x//g)  >= C1 + C2
            return l1 and l2 and l3

        def check(x):
            A = x // d1
            A_ = x - A
            B = x // d2
            B_ = x - B
            AIB = x // lcm(d1, d2)
            AuB = A + B - AIB
            A_IB_ = x - AuB
            cA = 0 if A_ - A_IB_ >= C1 else C1 - (A_ - A_IB_)
            cB = 0 if B_ - A_IB_ >= C2 else C2 - (B_ - A_IB_)

            return A_IB_ >= cA + cB



        l, h, g = 1, 10e9, lcm(d1, d2)
        while l < h:
            m = l + (h - l) // 2

            if check(m):
                h = m
            else:
                l = m + 1

        return int(l)