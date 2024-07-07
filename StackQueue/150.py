class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        num_stack = []

        for t in tokens:
            if t.lstrip("-").isdigit():
                num_stack.append(t)
            else:
                print(num_stack)
                n1 = num_stack.pop()
                n2 = num_stack.pop()
                num_stack.append(str(int(eval(n2+t+n1))))


        return int(num_stack[-1])


print(Solution().evalRPN(tokens =["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
#print(Solution().evalRPN(tokens = ["4","13","5","/","+"]))
#print(Solution().evalRPN(tokens = ["2","1","+","3","*"]))
