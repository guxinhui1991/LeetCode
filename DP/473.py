class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """

        if(sum(matchsticks)%4): return False

        target = sum(matchsticks)//4
        matchsticks.sort(reverse=True)

        sides = [0]*4
        def checkLen(i):
            if i==len(matchsticks): return True
            for j in range(4):
                if (sides[j] + matchsticks[i]) <= target:
                    sides[j]+= matchsticks[i]
                    if checkLen(i+1):
                        return True
                    else:
                        sides[j] -= matchsticks[i]

            return False

        checkLen(0)

        return

