class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Lqueue for extra (
        # Rqueue for extra )
        Extraqueue = []
        N = len(s)
        for i in range(N):
            if not Extraqueue:
                Extraqueue.append(s[i])
            else:
                if s[i] == '(' or (s[i] == ')' and Extraqueue[-1] == ')'):
                    Extraqueue.append(s[i])
                elif s[i] == ')' and Extraqueue[-1] == '(':
                    Extraqueue.pop()
        return len(Extraqueue)
'''
            if not Rqueue:
                Rqueue.append(s[N-i-1])
            else:
                if s[N-i-1] == ')':
                    Rqueue.append(s[N-i-1])
                elif s[N-i-1] == '(' and Rqueue[-1] == ')':
                    Rqueue.pop()
'''


print(Solution().minAddToMakeValid('()))(('))
print(Solution().minAddToMakeValid('()'))
print(Solution().minAddToMakeValid('())'))
print(Solution().minAddToMakeValid('((('))