import functools
from typing import List


class Solution:
    def largestNumber_simplified(self, nums: List[int]) -> str:
        comp = lambda a, b: 1 if a + b > b + a else -1 if a + b < b + a else 0
        nums_str = [str(i) for i in nums]
        nums_str.sort(key=functools.cmp_to_key(comp), reverse= True)
        return ''.join(nums_str)


    def largestNumber(self, nums: List[int]) -> str:


        res = []
        nums_str = [str(i) for i in nums]
        def compare(s1, s2):
            return s1+s2 > s2+s1



        for i in nums_str:
            idx = len(res)
            for j, cur_str in enumerate(res):
                if compare(i, cur_str):
                    idx = j
                    break

            res.insert(idx, i)

        return ''.join(res)





print(Solution().largestNumber([3,30,34,5,9]))
print(Solution().largestNumber([128,12,320,32]))
print(Solution().largestNumber([10,2,9,39,17]))
print(Solution().largestNumber([10,2]))