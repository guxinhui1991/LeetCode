class Solution(object):
    def minSubArrayLen(self, target, nums):
        tmp_sum = 0
        cur_s = 0

        res = float('inf')
        for i in range(len(nums)):
            tmp_sum += nums[i]

            while(tmp_sum >= target):
                res = min(res, i - cur_s + 1)
                tmp_sum = tmp_sum - nums[cur_s]
                cur_s += 1

        return res if res!=float('inf') else 0

print(Solution().minSubArrayLen(target = 15, nums = [5,1,3,5,10,7,4,9,2,8]))
print(Solution().minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))