from typing import List


class Solution(object):

    #####################################
    #
    #   Apr 2023
    #
    #####################################
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result =[[]]
        for i in nums:
            #print(result)
            result += [[i]+arr for arr in result ]

        return result

class Solution2:

    #####################################
    #
    #   Dec 2023
    #
    #####################################
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res, curr = [], []

        def dfs(nums):
            res.append(curr.copy())
            for i,val in enumerate(nums):
                curr.append(val)
                dfs(nums[i + 1:])
                curr.pop()
            return

        dfs(nums)
        return res


print(Solution().subsets([1,2,3]))
print(Solution2().subsets([1,2,3]))