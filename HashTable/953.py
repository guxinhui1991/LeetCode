from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dic = {}
        for i, val in enumerate(order):
            order_dic[val] = i + 1
        order_dic[""] = 0

        def compareWords(w1, w2):
            nonlocal order_dic
            idx = 0
            l1, l2 = len(w1), len(w2)
            while idx < len(w1) and idx < len(w2) and w1[idx] == w2[idx]:
                idx += 1

            if l1 - idx > 0 and l2 - idx <= 0:
                return False
            elif idx < l2 and idx < l1 and order_dic[w1[idx]] > order_dic[w2[idx]]:
                return False

            return True

        for i in range(1, len(words)):
            if not compareWords(words[i - 1], words[i]):
                return False

        return True

