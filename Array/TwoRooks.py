def twoRooksMax(arr):
    n = len(arr)
    m = len(arr[0])

    # pre-compute 4 quadrants
    topLeft = computeQuadrantMax(arr, 0, 0, 1, 1, n, m)
    topRight = computeQuadrantMax(arr, 0, m - 1, 1, -1, n, -1)
    botLeft = computeQuadrantMax(arr, n - 1, 0, -1, 1, -1, m)
    botRight = computeQuadrantMax(arr, n - 1, m - 1, -1, -1, -1, -1)
    quadrants = [topLeft, topRight, botLeft, botRight]

    # compute the max for two rooks
    curMax = float('-inf')
    for i in range(0, n):
        for j in range(0, m):
            maxRook2 = float('-inf')
            diagonals = ((-1, -1), (-1, 1), (1, -1), (1, 1))
            for qd, dg in enumerate(diagonals):
                ii, jj = i + dg[0], j + dg[1]
                if 0 <= ii < n and 0 <= jj < m:
                    maxRook2 = max(maxRook2, quadrants[qd][ii][jj])
            curMax = max(curMax, arr[i][j] + maxRook2)

    return curMax


def computeQuadrantMax(arr, startRow, startCol, moveRow, moveCol, endRow, endCol):
    n = len(arr)
    m = len(arr[0])
    quadrant = [[0] * m for _ in range(n)]

    for i in range(startRow, endRow, moveRow):
        for j in range(startCol, endCol, moveCol):
            prevMax1 = float('-inf')
            if 0 <= i - moveRow < n:
                prevMax1 = quadrant[i - moveRow][j]
            prevMax2 = float('-inf')
            if 0 <= j - moveCol < m:
                prevMax2 = quadrant[i][j - moveCol]
            quadrant[i][j] = max(prevMax1, prevMax2, arr[i][j])

    return quadrant


A = [
    [0, 1, 5],
    [3, 0, 5],
    [1, 4, 1]
]
print(twoRooksMax(A))