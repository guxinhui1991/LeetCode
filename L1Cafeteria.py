from typing import List
import numpy as np
import math


# Write any import statements here
def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    S = sorted(S)
    res = 0
    start, space = 1, 0

    for s in S:
        space = s - start
        res = res + max(0, space // (K+1))
        start = s + K + 1
    if (S[-1] + K < N): res = res + (N - S[-1]) // (K + 1)
    return res


def getMaxAdditionalDinersCount1(N: int, K: int, M: int, S: List[int]) -> int:
    # Write your code here
    if N <= K: return 0
    S = sorted(S)
    possibleSeats = np.array([True] * N)
    for i in S:
        if (i <= K):
            possibleSeats[0: i+K+1] = False
        elif (i >= N - K):
            possibleSeats[i-K-1: N] = False
        else:
            possibleSeats[i-K-1: i+K] = False

    res = np.array([0] * len(possibleSeats))
    for i, val in enumerate(possibleSeats):
        if not val:
            res[i] = M
        if val:
            res[i] = M + 1 + getMaxAdditionalDinersCount1(N, K, M+1, sorted(S+[i+1]))

    return max(res)




def getMaxAdditionalDinersCountFinal(N: int, K: int, M: int, S: List[int]) -> int:
    S.sort()
    start, res = 1, 0
    S.append(N+K+1)
    for s in S:
        delta = s-K-start
        if delta > 0:
            res += math.ceil(delta / (K+1))
        start = s+K+1
    return res


print(getMaxAdditionalDinersCount(N = 10, K = 1, M = 2, S = [2, 6]))
print(getMaxAdditionalDinersCount(N = 15, K = 2, M = 3, S = [11, 6, 14]))

