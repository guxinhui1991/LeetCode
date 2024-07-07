from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def nextGreaterIndex(val, arr, start_index):
            N = len(arr)
            res = -1
            for i in range(start_index, N):
                if arr[i] > val:
                    return i
            return res

        t1 = [nextGreaterIndex(nums1[i], nums2, i) for i in range(len(nums1))]
        t2 = [nextGreaterIndex(nums2[i], nums1, i) for i in range(len(nums2))]

        ptr1, ptr2 = 0, 0
        res = []
        while k:

            if nums2[t1[ptr1]] >= nums1[t2[ptr2]] or t2[ptr2] < 0:
                res.append(nums2[t1[ptr1]])
                ptr1 += 1
                ptr2 = nextGreaterIndex(nums2[t1[ptr1]], nums2, ptr1)
            else:
                res.append(nums1[t2[ptr2]])
                ptr2 += 1
                ptr1 = nextGreaterIndex(nums1[t2[ptr2]], nums1, ptr2)


            k -= 1

        return res


print(Solution().maxNumber( nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5))