class Solution(object):
    def minRemoveToMakeValid(self, s):
        idx_list = []
        cur_stack = []
        for i, c in enumerate(s):
            if c == ')':
                if not cur_stack or cur_stack[-1] == ')':
                    idx_list.append(i)
                    cur_stack.append(c)
                    #Cookie.pop(i)
                elif cur_stack[-1] == '(':
                    idx_list.pop()
                    cur_stack.pop()
            elif c == '(':
                idx_list.append(i)
                cur_stack.append(c)

        return ''.join([ele for idx, ele in enumerate(s) if idx not in idx_list])


class Solution:
    def minRemoveToMakeValid_slow(self, s: str) -> str:
        res_idx = []
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    res_idx.append(i)

        return "".join(c for i, c in enumerate(s) if i not in res_idx and i not in stack)

    # Mar 10, 2024
    def minRemoveToMakeValid_fast(self, s: str) -> str:
        arr = list(s)

        q = []
        for i, c in enumerate(s):
            if c == "(":
                q.append(i)
            elif c == ")":
                if q:
                    q.pop()
                else:
                    arr[i] = ""
        for j in q:
            arr[j] = ""

        return "".join(arr)


print(Solution().minRemoveToMakeValid("))(("))