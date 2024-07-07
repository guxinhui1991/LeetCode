from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res, curr = [], []
        cur_count = 3

        def checkValid(s):
            if not s or len(s) >3 or (s[0] == "0" and len(s)> 1) or int(s) > 255: return False
            return True

        def backTracking(s, cur_count):

            if cur_count == 0 and checkValid(s):
                res.append(".".join(curr + [s]))
                return

            if cur_count == 0 and not checkValid(s):
                return


            for j in range(3):
                if checkValid(s[:j+1]):
                    curr.append(s[:j+1])
                    backTracking(s[j+1:], cur_count - 1)
                    curr.pop()

        backTracking(s, cur_count)


        return res


print(Solution().restoreIpAddresses("25525511135"))