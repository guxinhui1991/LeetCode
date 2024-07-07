from typing import List


class Solution:

    # By sorted string
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return list(d.values())


    # By tuple
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for w in strs:
            count = [0] * 26
            for i, c in enumerate(w):
                count[ord(c) - ord('a')] +=  1
            key = tuple(count)
            res[key] = res.get(key, []) + [w]
        return list(res.values())


print(Solution().groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams2(strs = ["eat","tea","tan","ate","nat","bat"]))

