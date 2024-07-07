class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """

        cur_stack = []

        for c in s:
            if c == ')':
                if not cur_stack or cur_stack[-1] == ')':
                    cur_stack.append(c)
                elif cur_stack[-1] == '(':
                    cur_stack.pop()
            else:
                cur_stack.append(c)

        return len(cur_stack)

    # Greedy method
    def minAddToMakeValid(self, s: str) -> int:
        res, count = 0, 0

        for c in s:
            if c == "(":
                count += 1
            else:
                count -= 1

            if count < 0:
                res += 1
                count = 0

        return count + res



print(Solution().minAddToMakeValid("()))(("))