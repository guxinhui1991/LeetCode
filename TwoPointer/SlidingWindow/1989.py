from typing import List


class Solution:
    def catchMaximumAmountofPeople(self, team: List[int], k: int) -> int:

        t, p = [], []
        for i,val in enumerate(team):
            if val: t.append(i)
            else: p.append(i)

        res = 0
        idx_p, idx_t = 0, 0
        while idx_p < len(p) and idx_t < len(t):
            if p[idx_p] - k <= t[idx_t] <= p[idx_p] + k:
                res += 1
                idx_p += 1
                idx_t += 1
            elif p[idx_p] + k < t[idx_t]:
                idx_p += 1
            elif p[idx_p] - k > t[idx_t]:
                idx_t += 1


        return res




