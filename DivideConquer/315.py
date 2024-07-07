from bisect import bisect_left
from typing import List


class Solution:
    # Retaining index
    def countSmaller(self, nums: List[int]) -> List[int]:

        N = len(nums)
        val_idx = [[val, idx] for idx, val in enumerate(nums)]
        res = [0] * N

        def merge_sort(l, r):
            if l >= r - 1: return

            m = (l + r) // 2
            merge_sort(l, m)
            merge_sort(m, r)
            merge(l, m, r)

        def merge(l, m, r):
            nonlocal val_idx, res
            i, j = l, m
            temp = []
            while i < m and j < r:
                if val_idx[i][0] <= val_idx[j][0]:
                    res[val_idx[i][1]] += j - m
                    temp.append(val_idx[i])
                    i += 1
                else:
                    temp.append(val_idx[j])
                    j += 1
            while i < m:
                res[val_idx[i][1]] += j - m
                temp.append(val_idx[i])
                i += 1

            while j < r:
                temp.append(val_idx[j])
                j += 1

            for i in range(l, r):
                val_idx[i] = temp[i - l]

        merge_sort(0, N)
        return res

    # Divide and conquer -- TLE
    def countSmaller2(self, nums: List[int]) -> List[int]:

        N = len(nums)
        nums_res, res = [i for i in nums], [0] * N

        def merge_sort(l, r):
            nonlocal res, nums, nums_res
            if l >= r: return
            m = l + (r - l) // 2
            merge_sort(l, m)
            merge_sort(m + 1, r)

            for i in range(l, m + 1):
                j = bisect_left(nums_res[m + 1:r + 1], nums[i])
                res[i] += j

            i, j = l, m + 1
            temp = []
            while i <= m and j <= r:
                if nums_res[i] < nums_res[j]:
                    temp.append(nums_res[i])
                    i += 1
                else:
                    temp.append(nums_res[j])
                    j += 1
            while i <= m:
                temp.append(nums_res[i])
                i += 1

            while j <= r:
                temp.append(nums_res[j])
                j += 1
            nums_res[l:r + 1] = temp

        merge_sort(0, N - 1)
        return res

print(Solution().countSmaller([5,1,6,2]))
print(Solution().countSmaller2([5,1,6,2]))