class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if(len(nums) < 3): return

        nums.sort()

        res = sum(nums[:3])
        for i in range(len(nums) - 2):
            j, k = i+1, len(nums) -1
            while(j<k):
                tmp = nums[i]+nums[j]+nums[k]
                if (abs(tmp - target) < abs(res - target)): res = tmp

                if(abs(tmp - target) == 0 ): return target
                elif(tmp > target): k-=1
                elif(tmp < target): j+=1

        return res


print(Solution().threeSumClosest([-1000,-5,-5,-5,-5,-5,-5,-1,-1,-1] , -14))
print(Solution().threeSumClosest([-1,2,1,-4], 1))