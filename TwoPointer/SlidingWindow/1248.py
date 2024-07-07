from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def atMostK(k):
            l = r = 0
            res = count = 0
            while r < len(nums):
                count += nums[r] % 2
                while l <= r and count > k:
                    count -= nums[l] % 2
                    l += 1

                res += r - l
                r += 1
            return res

        return atMostK(k) - atMostK(k-1)

    # Sliding window optimized
    def numberOfSubarrays2(self, nums: List[int], k: int) -> int:

        l = 0
        cur = res = 0
        count = 0
        for r in range(len(nums)):
            if nums[r]%2:
                cur += 1
                count = 0

            while cur == k:
                cur -= nums[l]%2
                l += 1
                count += 1
            res += count

        return res

print(Solution().numberOfSubarrays([1,1,2,1,1], 3))
print(Solution().numberOfSubarrays(nums = [2,4,6], k = 1))