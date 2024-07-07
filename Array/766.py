from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        h, w = len(matrix), len(matrix[0])

        for i in range(w):
            x,y = 0, i
            while x<h-1 and y<w-1:
                if matrix[x][y]!=matrix[x+1][y+1]: return False
                x+=1
                y+=1

        for i in range(h):
            x,y = i, 0
            while x<h-1 and y<w-1:
                if matrix[x][y]!=matrix[x+1][y+1]: return False
                x+=1
                y+=1

        return True