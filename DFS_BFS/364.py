class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:

        res = 0
        max_depth = 1
        w, val = [], []
        for e in nestedList:

            stack = [(e, 1)]

            while stack:
                cur_len = len(stack)
                for _ in range(cur_len):

                    cur_e, cur_d = stack.pop()
                    if not cur_e.isInteger():
                        for item in cur_e.getList():
                            stack.append((item, cur_d + 1))
                    elif cur_e.isInteger():
                        val.append(cur_e.getInteger())
                        w.append(cur_d)
                    max_depth = max(max_depth, cur_d)

        w_new = [max_depth - d + 1 for d in w]
        return sum(w_new[i] * val[i] for i in range(len(val)))
