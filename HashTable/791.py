import collections


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic_order = {}
        for i, c in enumerate(order):
            dic_order[c] = i

        cur_dict = {}
        left_over = []
        for i, c in enumerate(s):

            if c in dic_order:
                cur_dict[dic_order[c]] = cur_dict.get(dic_order[c], []) + [c]
            else:
                left_over.append(c)

        res = []

        for k, v in sorted(cur_dict.items()):
            res += v
        res += left_over
        return "".join(res)



class Solution:
    def customSortString(self, S: str, T: str) -> str:
        c, s = collections.Counter(T), set(S)
        return ''.join(i * c[i] for i in S) + ''.join(i * c[i] for i in c if i not in s)


