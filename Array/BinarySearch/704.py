class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.bi_search(nums, 0, len(nums)-1, target)

    def bi_search(self, nums, l, r, target):
        if l > r: return -1
        if l == r: return l if nums[l] == target else -1

        mid = (l + r) // 2
        if target == nums[mid]: return mid
        elif target > nums[mid]:
            return self.bi_search(nums, mid+1, r, target)
        else:
            return self.bi_search(nums, l, mid, target)





print(Solution().search(nums = [-1,0,3,5,9,12], target = 13))