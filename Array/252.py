from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        N = len(intervals)
        for i in range(1, N):

            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True