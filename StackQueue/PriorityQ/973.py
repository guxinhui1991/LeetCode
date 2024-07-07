import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        N = len(points)
        if k == N: return points
        dis_dict = {}

        for i in range(N):
            p = points[i]
            dis = (p[0] ** 2 + p[1] ** 2)
            dis_dict[dis] = dis_dict.get(dis, []) + [p]

        val = sorted(dis_dict.keys())
        res = []
        i = 0
        while len(res) < k:
            while (dis_dict[val[i]]):
                res.append(dis_dict[val[i]].pop())
            i += 1
        return res

    def kClosest_Optimized(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        heapq.heapify(heap)

        for i, p in enumerate(points):
            dis = p[0]**2 + p[1]**2
            heapq.heappush(heap, (dis, p))
        res = []
        while k > 0:
            res.append(heapq.heappop(heap))
            k-=1

        return res


Solution().kClosest([[1,3],[-2,2],[2,-2]], 2)
Solution().kClosest_Optimized([[1,3],[-2,2],[2,-2]], 2)