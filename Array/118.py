class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if (numRows == 0): return []
        elif(numRows == 1): return [[1]]

        res = [[1]]
        for i in range(1, numRows):
            cur_list = res[i-1]
            res.append([1] + [i + j for i, j in zip(cur_list[1:], cur_list[:-1])] + [1])

        return  res