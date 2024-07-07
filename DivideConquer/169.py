class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return self.findElement(nums, 0, len(nums)-1)

    def findElement(self, nums, l, r):
        if (l == r): return nums[l]

        m = l + (r-l) // 2

        l_max= self.findElement(nums, l, m)
        r_max= self.findElement(nums, m+1 , r)

        if (l_max == r_max):
            return l_max
        else:
            return l_max if nums.count(l_max) > nums.count(r_max) else r_max



class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return
        cur = nums[0]
        count = 1
        for c in nums[1:]:
            if c == cur:
                count+=1
            else:
                if count != 0:
                    count-=1
                else:
                    count = 1
                    cur = c
        return cur



nums =[4,4,5]

print(Solution2().majorityElement(nums))

