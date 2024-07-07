class Solution:
    def maximumSwap(self, num: int) -> int:

        arr = list(str(num))
        N = len(arr)
        inf = float('inf')

        ptr = -1
        for i in range(1, N):
            if float(arr[i]) > float(arr[i-1]):
                ptr = i - 1
                break

        if ptr == -1: return num

        cur_max, idx = -inf, 0
        for i in range(ptr, N):
            if float(arr[i]) >= cur_max and float(arr[i]) > float(arr[ptr]):
                cur_max = float(arr[i])
                idx = i

        if idx == 0: return num

        for i in range(ptr):
            if float(arr[i]) < cur_max:
                ptr = i
                break


        arr[ptr], arr[idx] = arr[idx], arr[ptr]

        return int("".join(arr))

    # Optimized on the index swap finding process
    def maximumSwap2(self, num: int) -> int:
        arr = list(str(num))
        d = {}

        for i, c in enumerate(arr):
            d[int(c)] = i

        for i, c in enumerate(arr):
            for v in range(9, int(c), -1):
                if d.get(v, 0) > i:
                    arr[i], arr[d[v]] = arr[d[v]], arr[i]
                    return int("".join(arr))

        return num

    # Alternatively, loop from end of array
    #
    def maximumSwap3(self, num: int) -> int:
        arr = list(str(num))
        N = len(arr)

        m, n = N - 1, N - 1
        i_max = N - 1
        for i in range(N - 1, -1, -1):
            if arr[i] > arr[i_max]:
                i_max = i
            if arr[i] < arr[i_max]:
                m = i
                n = i_max
        arr[m], arr[n] = arr[n], arr[m]

        return int("".join(arr))


print(Solution().maximumSwap(99901))
print(Solution().maximumSwap(100))
print(Solution().maximumSwap(10909091))
print(Solution().maximumSwap(115))
print(Solution().maximumSwap(98368))
print(Solution().maximumSwap(2736))
print(Solution().maximumSwap(9973))