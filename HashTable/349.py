# Dec 14, 2023
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1 = {}
        for i in nums1:
            count1[i] = count1.get(i, 0) + 1

        count2 = {}
        for i in nums2:
            count2[i] = count2.get(i, 0) + 1

        return list(set(count1.keys()) & set(count2.keys()))

    def intersection2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))
