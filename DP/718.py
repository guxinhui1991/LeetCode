from typing import List


class Solution:
    # TLE

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        dp = [0 for i in range(N)]

        for i in range(N):
            cur_count = 0
            val = nums1[i]
            for j in range(len(nums2)):
                if nums2[j] == val:
                    tmp_count, tmp_index = 0, i
                    #tmp_count = 0
                    while j < len(nums2) and tmp_index < len(nums1) and nums2[j] == nums1[tmp_index]:
                        tmp_count +=1
                        j+=1
                    #    i+=1

                    cur_count = max(cur_count, tmp_count)

            dp[i] = max(dp[i], cur_count)

        return max(dp)

    def findLength_DP(self, nums1: List[int], nums2: List[int]) -> int:
        N1, N2 = len(nums1), len(nums2)
        dp =[[0 for _ in range(N2+1)] for _ in range(N1+1)]
        res = 0
        for i in range(1, N1+1):
            for j in range(1, N2+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > res: res = dp[i][j]

        return res

print(Solution().findLength_DP(nums1 = [1,2,3,2,1], nums2 = [1,2,3,4,7]))
print(Solution().findLength_DP(nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]))
print(Solution().findLength_DP([0,0,0,0,0], [0,0,0,0,0]))