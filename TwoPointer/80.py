from typing import List


class Solution:
    def removeDuplicates2(self, nums: List[int]) -> int:
        ptr_s, ptr_f= 2, 2
        N = len(nums)
        if N <= 1: return N

        while ptr_f < N:
            if nums[ptr_f] != nums[ptr_s-2]:
                nums[ptr_s] = nums[ptr_f]
                ptr_s += 1
            ptr_f += 1

        print(nums)
        return ptr_s
        # cur_val = nums[ptr_s]
        # count = 2 if nums[ptr_s]== nums[0] else 1
        # while ptr_f < N and ptr_s < N:
        #     if count == 1:
        #         count = count + 1 if nums[ptr_s] == cur_val else 1
        #         ptr_s += 1
        #         nums[ptr_s] = nums[ptr_f]
        #         ptr_f += 1
        #
        #     elif count == 2:
        #         while ptr_f < N and nums[ptr_f] == cur_val:
        #             ptr_f += 1
        #         count = 1
        #         ptr_s += 1
        #         if ptr_f ==N or ptr_s == N: break
        #         nums[ptr_s] = nums[ptr_f]
        #         cur_val = nums[ptr_f]
        #         ptr_s+=1
        # return ptr_s

    def removeDuplicates(self, nums: List[int]) -> int:
        ptr_s, ptr_f  = 1, 2
        N = len(nums)

        if N <= 1: return N

        while ptr_f < N:
            if nums[ptr_f] == nums[ptr_s] and nums[ptr_f] == nums[ptr_s-1]:
                ptr_f += 1

            else:
                ptr_s += 1
                nums[ptr_s] = nums[ptr_f]
                ptr_f += 1

        print(nums)
        return ptr_s+1



print(Solution().removeDuplicates([1,1,1,2,2,3]))
print(Solution().removeDuplicates2([1,1,1,2,2,3]))
print(Solution().removeDuplicates([0,0,1,1,1,1,2,3,3]))
print(Solution().removeDuplicates2([0,0,1,1,1,1,2,3,3]))