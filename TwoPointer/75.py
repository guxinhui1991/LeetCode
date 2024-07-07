from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        ptr1, ptr2, ptr3 = 0, 0, N-1

        while ptr2 <= ptr3:
            if nums[ptr2] == 0:
                nums[ptr2] = nums[ptr1]
                nums[ptr1] = 0
                ptr1 += 1
                ptr2 += 1

            elif nums[ptr2] == 2:
                nums[ptr2] = nums[ptr3]
                nums[ptr3] = 2
                ptr3 -= 1

            else:
                ptr2 += 1
        print(nums)
        return


Solution().sortColors(nums=[2,0,2,1,1,0])