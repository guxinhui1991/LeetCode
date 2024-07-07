from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], k: int) -> int:

        N = len(customers)

        res, cur = 0, 0
        for i in range(N):
            if grumpy[i] == 0:
                res += customers[i]
                cur += customers[i]
            else:
                cur += customers[i]

            if i - k >= 0 and grumpy[i - k] == 1:
                cur -= customers[i - k]

            res = max(res, cur)

        return res


print(Solution().maxSatisfied(customers = [4,10,10], grumpy = [1,1,0], k = 2))
print(Solution().maxSatisfied(customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], k = 3))
