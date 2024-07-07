from typing import List

# Apr 2023
class Solution2(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        N = len(nums)
        maxReach = nums[0]
        curReach = nums[0]
        res = 1
        for i in range(1, N):

            maxReach = max(maxReach, i + nums[i])
            if i == curReach:
                if i < N - 1:
                    res += 1
                    curReach = maxReach
                    if (curReach > N - 1): return res
                else:
                    return res

        return res
# Dec 2023
class Solution:

    def jump(self, nums: List[int]) -> int:

        N = len(nums)

        cur_reach, next_step_reach = 0, 0
        steps = 0
        for i in range(N):
            if cur_reach >= N-1 : break

            next_step_reach = max(next_step_reach, nums[i] + i)
            if i == cur_reach:
                cur_reach = next_step_reach
                steps += 1

        return steps

print(Solution().jump([2,0,2,0,1]))
print(Solution2().jump([2,0,2,0,1]))
print(Solution().jump([1,1,1,1]))
print(Solution2().jump([1,1,1,1]))
print(Solution().jump([2,3,1,1,4]))
print(Solution2().jump([2,3,1,1,4]))

