class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        res = 0
        s = sorted(s)
        for child in g:
            cookieidx = self.findSmallestCookie(s, child)

            if cookieidx >= 0:
                res = res + 1
                s.pop(cookieidx)

        return res

    def findSmallestCookie(self, s, target):
        for i, num in enumerate(s):
            if num >= target:
                return i
        return -1


print(Solution().findContentChildren([1,2,3], [1,1]))