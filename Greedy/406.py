import sys
from typing import List


class Solution:
    # Start from shortest person and place.
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = [[] for i in range(len(people))]

        people.sort()
        total = len(people)

        prev_pop, cur_level = -sys.maxsize, 1
        while people:
            cur_min = people.pop(0)
            cur_spots = [i for i in range(total) if res[i] == []]
            if cur_min[0] == prev_pop:
                res[cur_spots[cur_min[1] - cur_level]] = cur_min
                cur_level += 1
            else:
                res[cur_spots[cur_min[1]]] = cur_min
                cur_level = 1
            prev_pop = cur_min[0]

        return res

    # Queue method -- start from tallest person and insert
    def reconstructQueue1(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(-x[0], x[1]))

        res = []

        for p in people:
            res.insert(p[1], p)

        return res


print(Solution().reconstructQueue(people = [[0,0],[6,2],[5,5],[4,3],[5,2],[1,1],[6,0],[6,3],[7,0],[5,1]]))
print(Solution().reconstructQueue1(people = [[0,0],[6,2],[5,5],[4,3],[5,2],[1,1],[6,0],[6,3],[7,0],[5,1]]))