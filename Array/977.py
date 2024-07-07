class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        min_idx = 0
        min_val = abs(nums[0])
        for i in range(1, len(nums)):
            if(abs(nums[i]) < min_val):
                min_idx = i
                min_val = abs(nums[i])


        res = [nums[min_idx]**2]
        l_ptr, r_ptr = 1, 1

        for i in range(1, len(nums)):
            if min_idx - l_ptr < 0 :
                res.append(nums[min_idx + r_ptr]**2)
                r_ptr+=1
            elif min_idx + r_ptr > len(nums) - 1:
                res.append(nums[min_idx - l_ptr] ** 2)
                l_ptr+=1
            else:
                if abs(nums[min_idx - l_ptr])  < abs(nums[min_idx + r_ptr]):
                    res.append(nums[min_idx - l_ptr] ** 2)
                    l_ptr+=1
                else:
                    res.append(nums[min_idx + r_ptr] ** 2)
                    r_ptr+=1


        return res


print(Solution().sortedSquares([-4,-1,0,3,10]))