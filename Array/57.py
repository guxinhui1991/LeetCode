from typing import List


class Solution:
    def insert(self, ints: List[List[int]], newI: List[int]) -> List[List[int]]:
        i = 0
        N = len(ints)
        while i < N and ints[i][0] <= newI[0]:
            i += 1
        ints.insert(i, newI)

        def checkOverlap(i1, i2):
            if i1[1] >= i2[0]: return True
            return False

        def mergeIntervals(arr):
            res = []
            ptr = 0
            while ptr < len(arr):
                cur = arr[ptr]
                ptr += 1
                while ptr<len(arr) and checkOverlap(cur, arr[ptr]):
                    cur = [min(cur[0], arr[ptr][0]), max(cur[1], arr[ptr][1])]
                    ptr += 1
                ptr -= 1
                res.append(cur)
                ptr += 1
            return res

        return mergeIntervals(ints)

print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
print(Solution().insert([[1,3],[6,9]], [2,5]))
print(Solution().insert([[1,3],[6,9]], [4,5]))