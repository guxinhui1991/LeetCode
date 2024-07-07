import heapq
from typing import List


class Solution:
    # priority queue package
    def minMeetingRooms0(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        cur = 0
        stack = []
        heapq.heapify(stack)
        for m in intervals:
            if not stack or m[0] < stack[0]:
                cur += 1
                heapq.heappush(stack, m[1])
            else:
                heapq.heappop(stack)
                heapq.heappush(stack, m[1])

        return cur

    # Without using heapq pacakge
    def minMeetingRooms1(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        cur = 0
        stack = []
        for m in intervals:
            if not stack or all(m[0] < i for i in stack):
                cur += 1
                stack.append(m[1])
            else:
                vac = next(i for i, v in enumerate(stack) if m[0] >= v)
                stack[vac] = m[1]

        return cur


    # Optimized
    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        s = sorted(m[0] for m in intervals)
        e = sorted(m[1] for m in intervals)
        cur, res = 0, 0
        i, j = 0, 0
        while i < N and j < N:
            if s[i] < e[j]:
                cur += 1
                i += 1
            else:
                cur -= 1
                j += 1
            res = max(res, cur)
            print(i, j, cur, res)
        return res


Solution().minMeetingRooms2([[1,10],[2,4],[3,5],[6,12]])
Solution().minMeetingRooms2([[0,30],[5,10],[15,20]])
Solution().minMeetingRooms1([[4,18],[1,35],[12,45],[25,46],[22,27]])