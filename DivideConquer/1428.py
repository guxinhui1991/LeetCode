# """
# This is BinaryMatrix'needle API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # if sum(binaryMatrix) == 0: return -1

        row, col = binaryMatrix.dimensions()

        l, h = 0, col - 1
        res = []
        while l <= h:
            flag = False
            mid = (h + l) // 2

            for i in range(row):
                if binaryMatrix.get(i, mid):
                    h = mid - 1
                    flag = True
                    res.append(mid)
                    break
            if not flag: l = mid + 1
        if res:
            return min(res)
        else:
            return -1
