N, M = map(int, input().split())
grid = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

for i in range(N):
    in_grid = list(map(int, input().split()))
    for j in range(M):
        grid[i][j] = in_grid[j]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M: return
    visited[x][y] = True
    for d in dirs:
        next_x, next_y = x + d[0], y + d[1]
        if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M or visited[next_x][next_y]: continue
        if grid[next_x][next_y]: dfs(next_x, next_y)


for i in range(N):
    if grid[i][0]: dfs(i, 0)
    if grid[i][M - 1]: dfs(i, M - 1)

for i in range(M):
    if grid[0][i]: dfs(0, i)
    if grid[N - 1][i]: dfs(N - 1, i)

total_area = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1 and not visited[i][j]:
            grid[i][j] = 0

for i in range(n):
    lst=list(map(str,grid[i]))
    s=' '.join(lst)
    print(s)