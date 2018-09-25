class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        i, j = 0, length-1
        res_vec = []

        while j>i:
            res_vec.append(min(height[i], height[j])*(j-i))
            if height[i] < height[j]:
                i+=1
            elif height[i] >= height[j]:
                j-=1
        print(max(res_vec))
        return max(res_vec)

Solution().maxArea([1, 3, 4, 5, 6, 3])


