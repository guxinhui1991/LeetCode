from typing import List

class Solution:
    def __init__(self):
        self.kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }


    def letterCombinations(self, digits: str) -> List[str]:
        l = len(digits)
        cur, res = [], []
        if not digits: return res

        def backTracking(idx):
            nonlocal l
            if len(cur) == l:
                res.append("".join(cur))
                return

            for i in range(idx, l):
                for c in self.kvmaps[digits[i]]:
                    cur.append(c)
                    backTracking(i + 1)
                    cur.pop()

        backTracking(0)
        return res


print(Solution().letterCombinations("23"))