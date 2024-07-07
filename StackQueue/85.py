class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        N = len(matrix)
        #M = len(matrix[0])

        cur_nums = [int(v) for v in matrix[0]]
        res = [0] * N
        res[0] = self.largestRecangleArea(cur_nums)

        for i in range(1, N):
            for j, val in enumerate(matrix[i]):
                cur_nums[j] = cur_nums[j] + 1 if int(val) != 0 else 0
            res[i] = self.largestRecangleArea([int(v) for v in cur_nums])

        return max(res)




    def largestRecangleArea(self, nums):
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