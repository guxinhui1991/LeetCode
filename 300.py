class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = int((i + j) / 2)
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)

            print(x, tails)
        return size


#print(Solution().lengthOfLIS([1,3,5,2,8]))
#print(Solution().lengthOfLIS([1,3,5,2,8,4,6]))


class Solution2(object):
    # A naive Python implementation of LIS problem

    """ To make use of recursive calls, this function must return
     two things:
     1) Length of LIS ending with element arr[n-1]. We use
     max_ending_here for this purpose
     2) Overall maximum as the LIS may end with an element
     before arr[n-1] max_ref is used this purpose.
     The value of LIS of full array of size n is stored in
     *max_ref which is our final result


     Complexity: O(2 ^ N) worst case
     """
    # global variable to store the maximum
    global maximum

    def lis_at_n(self, arr, n):
        global maximum

        if n == 1:
            return 1
        max_at_n = 1

        for i in range(1, n):
            res = self.lis_at_n(arr, i)
            if arr[i - 1] < arr[n - 1] and res + 1 > max_at_n:
                max_at_n = res + 1

        maximum = max(maximum, max_at_n)
        return max_at_n


    def lis(self, arr):
        global maximum

        maximum = 1
        self.lis_at_n(arr, len(arr))
        return maximum

print(Solution2().lis([10, 22, 9, 33, 21, 50, 41, 60]))


# Dynamic programming Python implementation of LIS problem

# lis returns length of the longest increasing subsequence
# in arr of size n
class Solution3(object):
    '''
    Dynamic programming Python implementation  of LIS problem

    lis returns length of the longest
    increasing subsequence in arr of size n
    Complexity: O(N ^ 2)

    '''
    def lis(self, arr):
        lisLenAtIdx = [1] * len(arr)

        for i in range(1, len(arr)):
            for j in range(0, i):
                if arr[i] > arr[j] and lisLenAtIdx[i] < lisLenAtIdx[j] + 1:
                    lisLenAtIdx[i] = lisLenAtIdx[j] + 1
        return max(lisLenAtIdx)



class Solution4(object):
    '''
    Complexity: O(N * log(N))
    '''
    def lis(self, nums):
        tails = []

        for x in nums:
            i, j = 0, len(tails)
            while i != j:
                m = int((i + j) / 2)
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m

            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x
            size = max(i + 1, len(tails))
        return len(tails)


print(Solution3().lis([1, 2, 4, 3, 6]))
print(Solution4().lis([1, 2, 4, 3, 6]))
