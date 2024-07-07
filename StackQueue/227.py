class Solution:
    def calculate(self, s: str) -> int:


        prev_op, prev_val = "+", 0
        stack = []
        ptr = 0

        while ptr < len(s):
            if s[ptr].isdigit():
                prev_val = 10 * prev_val + int(s[ptr])

            if s[ptr] in ["*", "/", "+", "-"] or ptr == len(s) - 1:

                if prev_op == "+": stack.append(prev_val)
                elif prev_op == "-": stack.append(-prev_val)
                elif prev_op == "*": stack.append(stack.pop() * prev_val)
                elif prev_op == "/": stack.append(int(stack.pop()/prev_val))
                prev_op, prev_val = s[ptr], 0

            ptr += 1

        return sum(stack)

    def calculate_Official(self, s: str) -> int:

        prev = '+'
        stack = []
        cur = 0
        for i, c in enumerate(s):
            if str.isdigit(c):
                cur = 10 * cur + int(c)
            if c in ['+', '-', '*', '/'] or i == len(s)-1:

                if prev == '+': stack.append(cur)
                elif prev == '-': stack.append(-1 * cur)
                elif prev == '*': stack[-1] = stack[-1] * cur
                elif prev == '/': stack[-1] = int(stack[-1] / cur)
                prev, cur = c, 0

        return sum(stack)

print(Solution().calculate(s = "14-3/2"))
print(Solution().calculate(s = "0-2147483647"))
print(Solution().calculate(s = "3+2*2"))
print(Solution().calculate(s = " 3+5 / 2 "))
print(Solution().calculate(s = "2*3+4"))
print(Solution().calculate(s = " 42 "))
print(Solution().calculate(s = "3/2"))