from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        N = len(intervals)
        intervals.sort(key=lambda x:x[0])

        res = 0

        while intervals:
            cur_min = intervals.pop(0)
            cur_end = cur_min[1]
            while intervals and intervals[0][0] < cur_end:
                cur_min = intervals.pop(0)
                cur_end = min(cur_end, cur_min[1])
                res +=1

        return res
