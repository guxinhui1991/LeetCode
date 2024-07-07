from math import factorial
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:

        res = 0

        def get_d(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        for i in range(len(points)):
            d_points = {}
            p_i = points[i]
            for p_j in points[:i] + points[i + 1:]:
                d = get_d(points[i], p_j)
                d_points[d] = d_points.get(d, 0) + 1

            for k, v in d_points.items():
                if v >= 2:
                    res += v * (v - 1)
        return res


print(Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]]))