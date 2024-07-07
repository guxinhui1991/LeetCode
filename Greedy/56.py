# Oct 2022
from typing import List


class Solution(object):
    def insertRes(self, inlist, res):
        inL = inlist[0]
        inR = inlist[1]

        if not res : return [inlist]
        if inlist[0] > res[-1][1]:
            res.append(inlist)
            return res
        if inlist[1] < res[0][0]:
            inlist.append(res)
            return inlist

        for i, curPair in enumerate(res):

            if curPair[1] >= inlist[0] >= curPair[0]:
                res[i] = [curPair[0], max(curPair[1], inlist[1])]
                return res

        return res

    def merge(self, intervals):
        if not intervals: return []

        def myFunc(e):
            return e[0]

        intervals.sort(reverse=False, key=myFunc)

        res = [intervals[0]]

        for inList in intervals[1:]:
            res = self.insertRes(inList, res)
        return res

# Dec 2023
class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        res = []
        while intervals:
            cur_interval = intervals.pop(0)
            if not res or cur_interval[0] > res[-1][1]:
                res.append(cur_interval)
            else:
                res[-1][1] = max(cur_interval[1], res[-1][1])

        return res

test1 = [[1,3],[2,6],[8,10],[15,18]]
test2 = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
test3 = [[1,4], [4,5]]
print(Solution().merge(test1))
print(Solution2().merge(test1))
print(Solution().merge(test2))
print(Solution2().merge(test2))
print(Solution().merge(test3))
print(Solution2().merge(test3))