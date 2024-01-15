class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        res = {}
        for d in dominoes:
            key_d = min(d[0], d[1])*10 + max(d[0], d[1])
            res[key_d] = res.get(key_d, 0) + 1

        numPairs = 0
        for i in res.values():
            numPairs = numPairs + i * (i-1)/2

        return numPairs