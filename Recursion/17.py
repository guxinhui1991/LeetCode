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

        res, path = [], []
        #if not digits : return res


        def back_tracking(digit_iter, k):
            nonlocal res, path

            if len(path) == k:
                res.append("".join(path))
                return path

            for i, val in enumerate(digit_iter):
                for l in self.kvmaps[digit_iter[i]]:
                    path.append(l)
                    back_tracking(digit_iter[i+1:], k)
                    path.pop()

            return

        back_tracking(digits, len(digits))

        return res


print(Solution().letterCombinations("23"))