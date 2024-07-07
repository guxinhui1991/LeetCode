class Solution(object):
    def removeElement(self, nums, val):
        l_ptr = 0

        for r_ptr in range(len(nums)):
            if(nums[l_ptr] == val):
                l_ptr += 1
                nums[l_ptr] = nums[r_ptr]

        return l_ptr


    def removeElement2(self, nums, val):

        slow, fast = 0, 0

        while fast < len(nums):

            if(nums[fast] != val):
                nums[slow] = nums[fast]
                slow+=1
            fast += 1
        print(nums)
        return slow


print(Solution().removeElement2([0,1,2,2,3,0,4,2], 2))