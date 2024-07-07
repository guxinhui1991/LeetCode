# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        k = 1
        idx = 0
        while reader.get(idx + k) < target:
            k = k * 2

        l, r = idx, idx + k

        while l <= r:
            m = l + (r - l) // 2
            if reader.get(m) == target:
                return m
            elif reader.get(m) < target:
                l = m + 1
            elif reader.get(m) > target:
                r = m - 1

        return -1