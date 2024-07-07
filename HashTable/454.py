class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        res_1 = {}
        for i, n1 in enumerate(nums1):
            for j, n2 in enumerate(nums2):
                res_1[n1+n2] = res_1.get(n1+n2, 0) + 1

        res_2 = {}
        for i, n3 in enumerate(nums3):
            for j, n4 in enumerate(nums4):
                res_2[n3+n4] = res_2.get(n3+n4, 0) + 1

        res = 0
        for k1, v1 in res_1.items():
            for k2, v2 in res_2.items():
                if k1+k2 == 0:
                    res += v1*v2

        return res



nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]

print(Solution().fourSumCount(nums1, nums2, nums3, nums4))


nums1 = [-1, -1]
nums2 = [-1, 1]
nums3 = [-1, 1]
nums4 = [1, -1]

print(Solution().fourSumCount(nums1, nums2, nums3, nums4))

