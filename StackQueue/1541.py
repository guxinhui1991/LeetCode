class Solution:

    # stack solution
    def minInsertions(self, s: str) -> int:
        stack = []
        res, i = 0, 0
        N = len(s)

        while i < N:
            c = s[i]
            if c == ')':
                if not stack:
                    res += 1
                    stack.append(1)
                elif stack[-1] == 1:
                    stack.pop()
                elif stack[-1] == 2:
                    stack.pop()
                    stack.append(1)
            else:
                if not stack or stack[-1] == 2:
                    stack.append(2)
                else:
                    stack.pop()
                    res += 1
                    stack.append(2)
            i += 1

        while stack:
            res += stack.pop()
        return res


    # Greedy method
    def minInsertions2(self, s: str) -> int:

        count, res = 0, 0
        N = len(s)
        i = 0
        while i < N:

            if s[i] == "(":
                count += 1
            else:
                if i<N-1 and s[i+1]==")":
                    count -= 1
                    i += 1
                else:
                    res += 1
                    count -= 1

            if count < 0:
                res += 1
                count = 0
            i += 1

        res += 2 * count
        return res


print(Solution().minInsertions(s = ")))))))"))
print(Solution().minInsertions(s = "(()))"))

print(Solution().minInsertions(s = ")))()))))))((()))())))()))))()))()())((()()))()(())()())()()))))))()()((()))("))
print(Solution().minInsertions(s = "))())("))
print(Solution().minInsertions(s = "())"))



