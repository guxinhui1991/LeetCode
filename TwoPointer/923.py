from typing import List


class Solution:
    def threeSumMulti(self, nums: List[int], target: int) -> int:

        res = 0
        N = len(nums)
        nums.sort()
        for i in range(N):
            #if i > 0 and nums[i] == nums[i - 1]: continue
            val = nums[i]
            cur_res, count = 0, 1
            cur_target = target - val

            l, r = i + 1, N - 1
            while l < r:

                if nums[l] + nums[r] == cur_target:
                    if nums[l] != nums[r]:
                        l_count, r_count = 1, 1
                        temp = 1
                        # cur_res += 1
                        r -= 1
                        while r > l and nums[r] == nums[r+1]:
                            l_count += 1
                            r -= 1
                        l += 1
                        while l <= r and nums[l] == nums[l-1]:
                            r_count += 1
                            l += 1
                        cur_res += temp * l_count * r_count
                    else:
                        cur_res += (r - l) * (r - l + 1) // 2
                        break
                elif nums[l] + nums[r] < cur_target:
                    l += 1
                elif nums[l] + nums[r] > cur_target:
                    r -= 1

            # while i < N - 1 and nums[i + 1] == nums[i]:
            #     count += 1
            #     i += 1

            res += count * cur_res

        return res % (10 ** 9 + 7)


print(Solution().threeSumMulti(nums = [0,1,2,0,2] , target = 3))
print(Solution().threeSumMulti(nums = [1,1,2,2,3,3,4,4,5,5], target = 8))