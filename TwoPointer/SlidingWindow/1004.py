from typing import List


class Solution:
    # Dec 2023
    def longestOnes1(self, nums: List[int], k: int) -> int:
        N = len(nums)
        res, k = 0, k

        ptr_s, ptr_f = 0, 0
        while ptr_s < N:

            while ptr_f < N and (nums[ptr_f] or k):
                k -= nums[ptr_f] == 0
                ptr_f += 1
            res = max(res, ptr_f - ptr_s)
            if not nums[ptr_s]: k += 1
            ptr_s += 1

        return res

    # Feb 2024
    def longestOnes2(self, nums: List[int], k: int) -> int:


        N = len(nums)
        res, l = 0, 0
        cur = 0
        for r in range(N):
            if nums[r] == 0: cur += 1

            while cur > k:
                cur -= nums[l] == 0
                l += 1
            res = max(r-l+1, res)

        return res


print(Solution().longestOnes1(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))
print(Solution().longestOnes2(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))


class Solution_Official:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            # If we included a zero in the window we reduce the value of k.
            # Since k is the maximum zeros allowed in a window.
            k -= 1 - nums[right]
            # A negative k denotes we have consumed all allowed flips and window has
            # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
            if k < 0:
                # If the left element to be thrown out is zero we increase k.
                k += 1 - nums[left]
                left += 1
        return right - left + 1



print(Solution_Official().longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))
