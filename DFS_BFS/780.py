#   From root to target
#   TLE
class Solution1:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        def DFS(x, y):
            if x == tx and y == ty:
                return True
            elif x > tx or y > ty:
                return False
            else:
                return DFS(x + y, y) or DFS(x, x + y)

        return DFS(sx, sy)



#   Only one way from target backwards:
#   i.e, target (19, 12) --> parent can only be (7, 12)
#   Final step to check (tx, ty) --> (sx, sy)
#       if tx==sx : (1, 5) --> (1, 2)
#       if ty==sy : (5, 1) --> (2, 1)
#
class Solution2:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy:
            if tx > ty:
                tx %= ty
            elif ty > tx:
                ty %= tx
            else:
                break

        return (tx == sx and ty >= sy and (ty - sy) % sx == 0) or (ty == sy and tx >= sx and (tx - sx) % sy == 0)