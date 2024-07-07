class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cur_mem = set()

        while True:
            tmp = 0
            while n > 0:
                tmp += (n%10) ** 2
                n = n//10
            n = tmp

            if tmp == 1:
                return True
            else:
                if n in cur_mem: return False
                cur_mem.add(tmp)




print(Solution().isHappy(2))
print(Solution().isHappy(19))
