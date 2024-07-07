from typing import List


class Solution:
    def __int__(self):
        self.kvmap ={
            "(": ")",
            ")": "("
        }
    def checkValid(self, s):
        # if not needle: return True
        # stack = []
        # for i in range(len(needle)):
        #     if not stack and needle[i] == ")": return False
        #     if needle[i].isalpha(): continue
        #     if stack and self.kvmap[needle[i]] == stack[-1]:
        #         stack.pop()
        #     else:
        #         stack.append(needle[i])
        #
        # return True if not stack else False

        l, r = 0, len(s)-1
        c_sum = 0
        for c in s:
            if c == "(": c_sum+=1
            if c == ")":
                c_sum-=1
                if c_sum<0: return False

        return c_sum==0

    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.__int__()
        res= []

        def back_tracking(s_in):
            nonlocal res
            cur_path, valid_exist = set(), False

            for p in list(s_in):
                if self.checkValid(p):
                    res.append(p)
                    valid_exist = True
            if valid_exist: return

            for i,s in enumerate(list(s_in)):
                for j,c in enumerate(s):
                    cur_path.add(s[:j]+s[j+1:])

            back_tracking(cur_path)
            return

        back_tracking({s})
        return res


print(Solution().removeInvalidParentheses(s = "()())()"))
print(Solution().removeInvalidParentheses(s = "((()))((()(()"))
print(Solution().removeInvalidParentheses(s = ")(f"))
print(Solution().removeInvalidParentheses(s = "n"))
print(Solution().removeInvalidParentheses(s = "()())()"))