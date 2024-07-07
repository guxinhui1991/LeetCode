from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        if sum(nums)%k or k>len(nums): return False
        target = sum(nums) // k

        nums.sort(reverse= True)

        if any(i> target for i in nums): return False

        #visited = [0 if nums[i]!= target  else 1 for i in range(len(nums))]
        group = sum(val==target for val in nums)

        nums = sorted([nums[i] for i in range(len(nums)) if nums[i]!=target], reverse=True)
        visited = [0 for _ in range(len(nums))]
        def dfs(cur_sum, visited, group):
            nonlocal target, k
            if group == k: return True
            if cur_sum == target: return dfs(0, visited, group + 1)

            last = -1
            for i,val in enumerate(nums):
                if visited[i] or cur_sum + nums[i]>target: continue
                if nums[i] == last: continue
                visited[i] = 1
                last = visited[i]
                if dfs(cur_sum + nums[i], visited, group):
                    return True
                visited[i] = 0
            return False



        return dfs(0, visited, group)




print(Solution().canPartitionKSubsets(nums = [4,3,2,3,5,2,1], k=4))
print(Solution().canPartitionKSubsets(nums = [3,3,10,2,6,5,10,6,8,3,2,1,6,10,7,2], k=6))
print(Solution().canPartitionKSubsets(nums = [85,35,40,64,86,45,63,16,5364,110,5653,97,95], k=7))
print(Solution().canPartitionKSubsets(nums = [114,96,18,190,207,111,73,471,99,20,1037,700,295,101,39,649], k=4))