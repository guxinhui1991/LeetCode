class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)
                    continue

        return max_len


    # Greedy --- is it possible?
    def longestValidParentheses2(self, s: str) -> int:
        count = 0
        res, cur_max = 0, 0

        for c in s:

            if c == "(":
                count += 1
            else:
                count -= 1
                if count >= 0:
                    cur_max += 2

            if count < 0:
                cur_max = 0
                count = 0
            res = max(cur_max, res)
        return res
print(Solution().longestValidParentheses2("()(()"))