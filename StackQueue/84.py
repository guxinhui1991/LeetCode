class Solution(object):
    def largestRectangleArea(self, nums):
        """
        :type heights: List[int]
        :rtype: int
        """

        res = 0
        length = len(nums)

        stk = []
        stk.append((0, nums[0]))
        max_area = nums[0]

        for i in range(1, length):
            idx, val = stk[-1]

            if nums[i] < val:
                while stk and nums[i] < val:
                    idx, val = stk.pop()
                    max_area = max(max_area, (i - idx) * val)
                    if stk:
                        val = stk[-1][1]
                stk.append((idx, nums[i]))
            else:
                stk.append((i, nums[i]))

        while stk:
            idx, val = stk.pop()
            max_area = max(max_area, (length - idx) * val)

        return max_area


