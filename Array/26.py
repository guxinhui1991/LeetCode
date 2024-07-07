class Solution(object):
    def removeDuplicates(self, nums):
        cur = set()

        slow, fast = 0, 0
        for fast in range(len(nums)):

            if nums[fast] not in cur:
                nums[slow] = nums[fast]
                slow += 1
                cur.add(nums[fast])

        nums[slow:] = ['_' for _ in nums[slow:]]
        return slow

    def removeDuplicates2(self, nums):
        s, f = 0, 1
        while f < len(nums):
            while f < len(nums) and nums[s]==nums[f]:
                f += 1
            if f == len(nums): break
            s += 1
            nums[s] = nums[f]
            f += 1

        return s



print(Solution().removeDuplicates([1,1,2]))