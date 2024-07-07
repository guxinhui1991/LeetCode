from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cur_dict = {0: [0]}
        cur_sum = 0
        for i, val in enumerate(nums):
            cur_sum += val
            cur_rem = cur_sum % k
            if cur_rem not in cur_dict:
                ################################################
                #
                #   set value to be (i+1) to pass the case {nums = [1, 0, 1], k = 3}
                #   cur_rem will be same for index 0, 1
                #   {nums = [1, 0, 0, 1], k = 3}  --> [0,0] valid
                #   {nums = [1, 0, 1], k = 3}  --> [1,0] invalid
                #
                ################################################
                cur_dict[cur_rem] = [i + 1]
            elif cur_dict[cur_rem][-1] < i:
                return True
        return False

Solution().checkSubarraySum([23,2,4,6,6], 7)