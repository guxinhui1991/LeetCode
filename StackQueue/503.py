from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        #val_max = max(nums)
        nums_duplicate = nums + nums
        stack, res = [], [-1 for _ in range(len(nums_duplicate))]
        for i in range(len(nums_duplicate)):
            val = nums_duplicate[i]

            while stack and val>nums_duplicate[stack[-1]]:
                cur_i = stack.pop()
                res[cur_i] = nums_duplicate[i]
            stack.append(i)

        return res[:len(nums)]

print(Solution().nextGreaterElements([1,2,1]))