class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        numPpl = len(ratings)
        resCandies = [1] * numPpl

        resLtoR = [1] * numPpl
        resRtoL = [1] * numPpl

        for i in range(1, numPpl):
            # Going forward from left to right
            if(ratings[i] > ratings[i-1]):
                resLtoR[i] = resLtoR[i-1] + 1

            # Going backward from right to left
            if(ratings[numPpl - i - 1] > ratings[numPpl - i]):
                resRtoL[numPpl - i - 1] = resRtoL[numPpl - i] + 1

        for i in range(numPpl):
            resCandies[i] = max(resLtoR[i], resRtoL[i])

        return sum(resCandies)


if __name__ == '__main__':
    print(Solution().candy([1, 0, 2]))
    print(Solution().candy([12, 4, 6, 8, 7]))