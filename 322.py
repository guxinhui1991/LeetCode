class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins = sorted(coins)
        N = len(coins)
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        for i, val in enumerate(coins):
            for j in range(val, amount+1):
                #if(j-val)>0:
                dp[j] = min(dp[j-val]+1, dp[j])

        return -1 if dp[-1] == float('inf') else dp[-1]

# Slow Algo
def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """

    if len(coins) <= 0 and amount != 0 : return -1
    if len(coins) and amount == 0 : return 0

    coins = sorted(coins, reverse = True)

    res = []
    for i, val in enumerate(coins):
        numTry = amount//val
        remAmount = amount%val
        if remAmount == 0:
            res.append(numTry)
            continue

        res_Try = []
        for j in range(numTry, -1, -1):
            res_Try.append(numTry + coinChange(coins[i+1:], remAmount + val*(numTry - j)))

        if  not res_Try or any(i < 0 for i in res_Try): continue

        res.append(min(i for i in res_Try if i >= 0))

    if any(i > 0 for i in res): return min(i for i in res if i > 0)


    return -1

print(Solution().coinChange(coins = [2147483647], amount = 2))
print(Solution().coinChange(coins = [1,2,5], amount = 11))
print(Solution().coinChange(coins = [2], amount = 3))
