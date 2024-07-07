from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        ptr1, ptr2 = m - 1, n - 1

        idx = m + n - 1

        while idx >= 0:

            if ptr1 >= 0 and ptr2 >= 0:
                if nums1[ptr1] > nums2[ptr2]:
                    nums1[idx] = nums1[ptr1]
                    ptr1 -= 1
                else:
                    nums1[idx] = nums2[ptr2]
                    ptr2 -= 1
            elif ptr1 >= 0:
                nums1[idx] = nums1[ptr1]
                ptr1 -= 1
            elif ptr2 >= 0:
                nums1[idx] = nums2[ptr2]
                ptr2 -= 1

            idx -= 1

        return

    # slightly better solution
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        idx = m + n - 1
        i, j = m-1, n-1
        while idx > 0 and i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[idx] = nums1[i]
                i-=1
            else:
                nums1[idx] = nums2[j]
                j-=1
            idx -= 1

        while j >= 0:
            nums1[idx] = nums2[j]
            j -= 1
            idx -= 1
        return