class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(n)]
        idx = 0
        while len(arr) > 1:
            cur_n = len(arr)
            arr.pop((idx + k - 1) % cur_n)
            idx = (idx + k - 1) % cur_n
        return arr[0]

print(Solution().findTheWinner(5, 2))