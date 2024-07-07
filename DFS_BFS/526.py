import timeit
from functools import lru_cache


class Solution:

    # Backtracking -- TLE
    def countArrangement(self, N: int) -> int:
        def checkbeautiful(w):
            if not w: return False
            p = 0
            while p < len(w):
                if w[p] % (p + 1) and (p + 1) % w[p]:
                    return False
                p += 1
            return True

        nums = [i+1 for i in range(N)]
        res = 0
        cur = []

        def DFS(arr):
            nonlocal res
            if checkbeautiful(cur) and len(cur) == N:
                res += 1
            if len(cur) == N: return

            for j in range(len(list(arr))):
                cur.append(list(arr)[j])
                DFS(tuple(list(arr)[:j] + list(arr)[j+1:]))
                cur.pop()
            return

        DFS(tuple(nums))
        return res



    # Backtracking -- slightly Efficient
    def countArrangement1(self, N: int) -> int:
        nums = [i+1 for i in range(N)]
        res = 0
        def swap(i, j):
            nonlocal nums
            temp  = nums[j]
            nums[j] = nums[i]
            nums[i] = temp

        def DFS(arr, i):
            nonlocal res
            if i == N: res += 1

            for j in range(i, N):
                swap(i, j)
                if not (arr[i] % (i + 1) and (i + 1) % arr[i]):
                    DFS(arr, i + 1)
                swap(i, j)

        DFS(nums, 0)
        return res


    # Backtracking -- Status of list
    def countArrangement2(self, N: int) -> int:
        nums = [i+1 for i in range(N)]
        visited = [False for _ in range(N)]
        res = 0

        def DFS(i):
            nonlocal nums, res, visited
            if i == N:
                res += 1

            for j in range(N):
                if not visited[j]:
                    if not (nums[i] % (j + 1) and (j + 1) % nums[i]):
                        visited[j] = True
                        DFS(i + 1)
                        visited[j] = False

        DFS(0)
        return res

#print(Solution().countArrangement(1))
#print(Solution().countArrangement(2))
#print(Solution().countArrangement(10))

start = timeit.default_timer()

print(Solution().countArrangement1(1))
print(Solution().countArrangement1(2))
print(Solution().countArrangement1(15))

stop = timeit.default_timer()
print('Time: ', stop - start)

start = timeit.default_timer()

print(Solution().countArrangement2(1))
print(Solution().countArrangement2(2))
print(Solution().countArrangement2(15))

stop = timeit.default_timer()
print('Time: ', stop - start)