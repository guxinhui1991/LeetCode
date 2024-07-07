from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        ptr_a, ptr_b = 0, 0
        len_a, len_b = len(firstList), len(secondList)
        res = []
        while ptr_a < len_a and ptr_b < len_b:
            l = max(firstList[ptr_a][0], secondList[ptr_b][0])
            h = min(firstList[ptr_a][1], secondList[ptr_b][1])

            if l <= h:
                res.append([l, h])

            if firstList[ptr_a][1] > secondList[ptr_b][1]:
                ptr_b += 1
            else:
                ptr_a += 1

        return res