# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        N = reader.length()
        # l, r = 0, N//2 - 1
        # x, y = r + 1, N - 1

        l, r = 0, N - 1
        while r - l + 1 >= 3:

            k = (r - l + 1) // 3
            res = reader.compareSub(l, l + k - 1, l + k, l + k * 2 - 1)

            if res == 0:
                l = l + k * 2
            elif res == 1:
                r = l + k - 1
            elif res == -1:
                l = l + k
                r = l + k * 2 - 1
        if (l == r):
            return l

        res = reader.compareSub(l, l, r, r)
        if res == 1:
            return l
        else:
            return r



