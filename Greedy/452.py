from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort()

        num = 0

        while points:
            cur_min = points.pop(0)
            arrow = cur_min[1]
            while points and points[0][0] <= arrow:
                cur_min = points.pop(0)
                arrow = min(cur_min[1], arrow)

            num += 1

        return num

print(Solution().findMinArrowShots(points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]))
print(Solution().findMinArrowShots(points = [[10,16],[2,8],[1,6],[7,12]]))