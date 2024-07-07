from typing import List


class Solution:
    """
    :type Children: List[int]
    :type Cookie: List[int] 
    :rtype: int
    """

    # Greedy11
    # Outer loop to be Children : fixed,  moving backwards
    #   backwards - Fill large cookie to large child
    def findContentChildren1(self, Children: List[int], Cookie: List[int]) -> int:
        Children.sort()
        Cookie.sort()
        res, idx = 0, len(Cookie) - 1
        for i in range(len(Children) - 1, -1, -1):
            if (idx >= 0 and Cookie[idx] >= Children[i]):
                idx -= 1
                res += 1
        return res

    # Greedy 2
    # Outer loop to be Cookie : fixed, moving forwards
    #   forwards - Fill small cookie to small child first
    def findContentChildren2(self, Children: List[int], Cookie: List[int]) -> int:
        Children.sort()
        Cookie.sort()
        res, idx = 0, 0
        for i in range(len(Cookie)):
            if (idx < len(Children) and Cookie[i] >= Children[idx]):
                idx += 1
        return idx

print(Solution().findContentChildren1([10,9,8,7], [5,6,7,8]))
print(Solution().findContentChildren2([10,9,8,7], [5,6,7,8]))
