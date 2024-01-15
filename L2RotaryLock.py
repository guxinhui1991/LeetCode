from typing import List


# Write any import statements here


# Case '797'
# should not compare only current state
def getMinCodeEntryTime_incorrect(N: int, M: int, C: List[int]) -> int:
    # Write your code here
    cur1 = 1
    cur2 = 1
    totalTime = 0
    for idx, val in enumerate(C):
        move1 = shortestTime(idx, cur1, N)
        move2 = shortestTime(idx, cur2, N)
        totalTime = totalTime + min(move1, move2)

        if (move1 < move2):
            cur1 = val
        else:
            cur2 = val

    return totalTime


'''
global cur1
if cur1 is None: cur1 = 1
global cur2
if cur2 is None: cur2 = 1
'''


def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    # Write your code here
    C =[1] + C
    totalTime = [[0]*(M+1) for _ in range(M+1)]
    totalTime[0][0] = shortestTime(1, C[0], N)

    timeOneLock = [0 for _ in range(M+1)]
    # Base case: Keep using one lock
    for i in range(M):
        timeOneLock[i+1] = timeOneLock[i] + shortestTime(C[i], C[i+1], N)

    for i in range(1, M+1):
        for j in range(i):
            if j == 0:
                totalTime[i][j] = timeOneLock[i]
            elif (int(j) == int(i-1)):
                totalTime[i][j] = min([totalTime[i-1][k] + shortestTime(C[k], C[i], N) for k in range(j)])
            else:
                totalTime[i][j] = totalTime[i-1][j] + shortestTime(C[i-1], C[i], N)


    return min(totalTime[M][:M])


def shortestTime(i, j, N):
    if i > j:
        return min(i - j, j + N - i)
    elif i < j:
        return min(j - i, i + N - j)
    return 0


print(getMinCodeEntryTime(N=10, M=3, C=[7, 9, 7]))
print(getMinCodeEntryTime(N=10, M=4, C=[9, 4, 4, 8]))
