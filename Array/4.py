from typing import List


class Solution:
    #
    #   O(M + N)
    #
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        total_len = m + n
        res = []
        i, j = 0, 0
        for its in range(total_len):
            if i < m and j < n:
                if (nums1[i] < nums2[j]):
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1

            elif i == m:
                res += nums2[j:]
                break;

            elif j == n:
                res += nums1[i:]
                break;

        print(res)
        if total_len % 2:
            return res[int(total_len / 2)]
        else:
            return (res[int(total_len / 2) - 1] + res[int(total_len / 2)]) / 2




    #
    #   O(log(M + N))
    #
    def findMedianSortedArrays2(self, A: List[int], B: List[int]) -> float:
        n1, n2 = len(A), len(B)

        if n1 > n2: return self.findMedianSortedArrays(B, A)

        l, r = 0, n1
        k = (n1 + n2 + 1) // 2
        while l < r:
            m1 = l + (r - l) // 2
            m2 = k - m1
            if A[m1] < B[m2 - 1]:
                l = m1 + 1
            else:
                r = m1

        m1, m2 = l, k - l

        c1 = max(float('-inf') if m1 <= 0 else A[m1 - 1], float('-inf') if m2 <= 0 else B[m2 - 1])

        if (n1 + n2) % 2 == 1: return c1
        c2 = min(float('inf') if m1 >= n1 else A[m1], float('inf') if m2 >= n2 else B[m2])
        return (c1 + c2) / 2


print(Solution().findMedianSortedArrays2([1,2], [3,4]))