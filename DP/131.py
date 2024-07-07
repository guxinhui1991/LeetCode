from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1: return [[s[0]]]
        return [[s[0]] + l for l in self.partition(s[1:])]






print(Solution().partition("aab"))
print(Solution().partition("a"))
