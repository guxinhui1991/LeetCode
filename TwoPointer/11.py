class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        i, j = 0, length-1
        res = 0.0

        while j>i:
            res = max(res, min(height[i], height[j])*(j-i))
            if height[i] < height[j]:
                i+=1
            elif height[i] >= height[j]:
                j-=1
        return res


height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))