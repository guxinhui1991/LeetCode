from typing import List


class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)

        cur_dic = {}
        for i in range(k):
            cur_dic[nums[i]] = cur_dic.get(nums[i], 0) + 1

        res = [0] * (N - k + 1)
        res[0] = len(cur_dic.keys())
        l, r = 0, k
        for i in range(1, N - k + 1):
            res[i] = res[i - 1]
            if nums[l] != nums[r]:
                if nums[r] in cur_dic:
                    cur_dic[nums[r]] += 1
                else:
                    cur_dic[nums[r]] = 1
                    res[i] += 1

                if nums[l] in cur_dic:
                    cur_dic[nums[l]] -= 1
                    if cur_dic[nums[l]] == 0:
                        res[i] -= 1
                        del cur_dic[nums[l]]
            l += 1
            r += 1

        return res