from typing import List


class Solution:
    # Sliding Window 1 -- count zeros
    def numSubarraysWithSum0(self, nums: List[int], goal: int) -> int:

        N = len(nums)
        post_zeros = [0] * N
        count = 0
        for i in range(N-1, -1, -1):
            post_zeros[i]= count
            if nums[i] == 0: count += 1
            else: count = 0

        r = 0
        res, cur_sum = 0, 0
        for i in range(N):
            while r <= i or (r < N and cur_sum < goal):
                cur_sum += nums[r]
                r += 1
            if cur_sum == goal:
                res += 1 + post_zeros[r-1]

            cur_sum -= nums[i]
        return res


    # Sliding Window 2 -- AtMostK

    def numSubarraysWithSum1(self, nums: List[int], goal: int) -> int:

        def atMostK(k):
            nonlocal  nums
            if k < 0: return 0
            res = l = 0
            for i in range(len(nums)):
                k -= nums[i]
                while k < 0:
                    k += nums[l]
                    l += 1

                res += i - l + 1
            return res

        def atMostK(k):
            res = cur = 0
            l = r = 0
            while r < len(nums):
                cur += nums[r]
                while l <=r and cur > k:
                    cur -= nums[l]
                    l += 1
                res += r-l+1
                r+= 1
            return res

        return atMostK(goal) - atMostK(goal - 1)

    def numSubarraysWithSum2(self, nums: List[int], goal: int) -> int:
        cur_sum ={0 : 1}
        res = cur = 0
        for i,v in enumerate(nums):
            cur += v
            res += cur_sum.get(cur - goal, 0)
            cur_sum[cur] = cur_sum.get(cur, 0) + 1
        return res



print(Solution().numSubarraysWithSum0([1,0,1,0,1], 2))
print(Solution().numSubarraysWithSum1([1,0,1,0,1], 2))
print(Solution().numSubarraysWithSum2([1,0,1,0,1], 2))

print(Solution().numSubarraysWithSum0([0,0,0,0,1], 2))
print(Solution().numSubarraysWithSum1([0,0,0,0,1], 2))
print(Solution().numSubarraysWithSum2([0,0,0,0,1], 2))

print(Solution().numSubarraysWithSum0([0,0,0,0,0,0,1,0,0,0],  0))
print(Solution().numSubarraysWithSum1([0,0,0,0,0,0,1,0,0,0],  0))
print(Solution().numSubarraysWithSum2([0,0,0,0,0,0,1,0,0,0],  0))

print(Solution().numSubarraysWithSum0([0,0,0,0,0], 0))
print(Solution().numSubarraysWithSum1([0,0,0,0,0], 0))
print(Solution().numSubarraysWithSum2([0,0,0,0,0], 0))
