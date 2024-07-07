from typing import List


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        stack = []
        res = 0

        for e in nestedList:

            cur_depth = 1
            stack.append((e, cur_depth))

            while stack:
                cur_len = len(stack)

                for _ in range(cur_len):
                    cur_e, depth_e = stack.pop(0)
                    if cur_e.isInteger():
                        res += depth_e * cur_e.getInteger()
                    else:
                        for item in cur_e.getList():
                            stack.append((item, depth_e + 1))

        return res


