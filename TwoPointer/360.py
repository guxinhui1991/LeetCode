from typing import List


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:


        def f(x):
            nonlocal a,b,c
            return a * x**2 + b * x + c


        if a == 0:
            return [f(i) for i in nums] if b > 0 else [f(i) for i in nums][::-1]


        mid = -b/2/a
        flag = a > 0
        N = len(nums)
        l, r = 0, N - 1
        res = [0] * N
        idx = 0
        while l <= r:
            if nums[r] < mid:
                res[idx] = f(nums[l])
                l += 1
            elif nums[l] > mid:
                res[idx] = f(nums[r])
                r -= 1
            else:
                if abs(nums[r] - mid) > abs(nums[l] - mid):
                    res[idx] = f(nums[r])
                    r -= 1
                else:
                    res[idx] = f(nums[l])
                    l += 1
            idx += 1

        return res[::-1] if flag else res