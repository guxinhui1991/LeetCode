from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        dict_len = {}
        for i, s in enumerate(strings):
            dict_len[len(s)] = dict_len.get(len(s), []) + [(i, [(ord(i) + 1 - ord(s[0])) % 26 for i in list(s)])]

        dict_len = dict(sorted(dict_len.items()))

        dict_res = {}
        res = []
        for s_len, s_list in dict_len.items():
            cur_res = []
            s_list.sort()
            # index_list, val_list = s_list

            cur_res = s_list[0][1]
            cur_res_index = [s_list[0][0]]
            for i in range(1, len(s_list)):
                if any(s_list[i][1][j] != cur_res[j] for j in range(len(cur_res))):
                    res.append(sorted([strings[i] for i in cur_res_index]))
                    cur_res = s_list[i][1]
                    cur_res_index = [s_list[i][0]]
                else:
                    cur_res_index.append(s_list[i][0])
            res.append(sorted([strings[i] for i in cur_res_index]))
        return res


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dict_len = {}
        for i, s in enumerate(strings):
            cur_list = tuple([(ord(i) + 1 - ord(s[0])) % 26 for i in list(s)])
            dict_len[cur_list] = dict_len.get(cur_list, []) + [i]

        dict_len = dict(sorted(dict_len.items()))
        return [[strings[i] for i in val] for val in dict_len.values()]



