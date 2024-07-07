from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        N = len(nums)

        over = 0
        cur_dic = {0 : -1}
        for i in range(N):
            if nums[i]:
                over += 1
            else:
                over -= 1
            if over in cur_dic:
                res = max(i - cur_dic[over], res)
            else:
                cur_dic[over] = i

        return res

