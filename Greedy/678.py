class Solution:

    # Think about case : s = "***((("
    def checkValidString(self, s: str) -> bool:
        stack = []
        count = 0
        for i, c in enumerate(s):
            if c == ")":
                if not stack or stack[-1] == ")":
                    stack.append(c)
                else:
                    stack.pop()
            elif c == "(":
                stack.append(c)
            else:
                count += 1

        return count >= len(stack)

    def checkValidString_official(self, s: str) -> bool:

        lo = hi = 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0: break
            lo = max(lo, 0)

        return lo == 0
Solution().checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())")