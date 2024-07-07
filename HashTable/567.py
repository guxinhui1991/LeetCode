from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l1 = len(s1)
        l2 = len(s2)

        if l2 < l1: return False

        f1 = Counter(s1)

        for i, c in enumerate(s2):
            if c in f1:
                if Counter(s2[i:i + l1]) == f1:
                    return True

        return False


print(Solution().checkInclusion("ab", "eidbaooo"))