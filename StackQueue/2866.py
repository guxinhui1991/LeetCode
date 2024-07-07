from typing import List


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        N = len(maxHeights)

        def getPeakSum(inArr):
            nonlocal N
            stack = [-1]

            l = [0] * N
            cur_max = 0
            for i in range(N):
                while len(stack) > 1 and inArr[i] < inArr[stack[-1]]:
                    cur = stack.pop()
                    prev = stack[-1]
                    cur_max -= inArr[cur] *(cur - prev)
                cur_max += inArr[i] * (i -stack[-1])
                stack.append(i)
                l[i] = cur_max

            return l

        l = getPeakSum(maxHeights)
        r = getPeakSum(maxHeights[::-1])[::-1]


        return max([l[i]+r[i]-maxHeights[i] for i in range(N)])



    # lee215
    def maximumSumOfHeights2(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)

        left = [0] * n
        stack = [-1]
        cur = 0
        for i in range(n):
            while len(stack) > 1 and maxHeights[stack[-1]] > maxHeights[i]:
                j = stack.pop()
                cur -= (j - stack[-1]) * maxHeights[j]
            cur += (i - stack[-1]) * maxHeights[i]
            stack.append(i)
            left[i] = cur

        stack = [n]
        res = cur = 0
        for i in range(n - 1, -1, -1):
            while len(stack) > 1 and maxHeights[stack[-1]] > maxHeights[i]:
                j = stack.pop()
                cur -= -(j - stack[-1]) * maxHeights[j]
            cur += -(i - stack[-1]) * maxHeights[i]
            stack.append(i)
            res = max(res, left[i] + cur - maxHeights[i])

        return res


Solution().maximumSumOfHeights(maxHeights = [6,5,3,9,2,7])
Solution().maximumSumOfHeights(maxHeights = [5,3,4,1,1])