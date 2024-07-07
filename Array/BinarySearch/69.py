class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: return 1
        l, h = 0, x-1

        while l < h-1:
            m = l + (h-l)//2
            if m*m == x: return m
            elif m*m <x:
                l = m
            elif m*m >x:
                h = m -1

        return h if h*h <= x else l