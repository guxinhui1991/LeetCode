from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        N = len(heights)
        stack = [0]

        for i in range(1, N):
            while stack and heights[i] >= heights[stack[-1]]:
                stack.pop()
            stack.append(i)
        return stack


