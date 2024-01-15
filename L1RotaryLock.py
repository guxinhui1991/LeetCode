from typing import List


# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    # Write your code here
    cur = 1
    totalTime = 0
    for i in C:
        totalTime = totalTime + shortestTime(i, cur, N)
        cur = i

    return totalTime


def shortestTime(i, j, N):
    if i > j:
        return min(i - j, j + N - i)
    elif i < j:
        return min(j - i, i + N - j)
    return 0


print(getMinCodeEntryTime(N=10, M=4, C=[9, 4, 4, 8]))
