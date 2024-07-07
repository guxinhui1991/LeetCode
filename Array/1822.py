class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if (0 in nums):
            return 0
        else:
            return -1 if sum(x < 0 for x in nums) % 2 else 1