from typing import List


class Solution(object):
    # Jan 2019
    # two points method
    def trap(self, height):
        res = 0
        maxL, maxR = 0, 0
        l, r = 0, len(height) - 1

        while (l < r):
            if height[l] <= height[r]:
                if height[l] > maxL:
                    maxL = height[l]
                else:
                    res += maxL - height[l]
                l += 1
            else:
                if height[r] > maxR:
                    maxR = height[r]
                else:
                    res += maxR - height[r]
                r -= 1
        return res



    # Dec 2023
    # StackQueue method
    def trap(self, height):
        # start to the largest tile
        asc_arr = []
        asc_arr_index = []
        for i, val in enumerate(height):
            if not asc_arr or val >= asc_arr[-1]:
                asc_arr.append(val)
                asc_arr_index.append(i)


        res = 0
        for idx in range(len(asc_arr) - 1):
            prev_val = asc_arr[idx]
            next_val = asc_arr[idx+1]

            prev_index = asc_arr_index[idx] + 1
            next_index = asc_arr_index[idx+1]

            tmp = 0
            while(prev_index < next_index):
                tmp += prev_val - height[prev_index]
                prev_index += 1
            res += tmp

        if(len(height) - asc_arr_index[-1] <=1 ):
            return res
        else:
            return res +self.trap(height[asc_arr_index[-1]: ][::-1])

# Cleaner stack method
class Solution2:
    def trap(self, height: List[int]) -> int:

        stack = [0]
        res = 0

        for i in range(1, len(height)):
            val = height[i]
            # Case 1: current value < top of stack
            if val < height[stack[-1]]:
                stack.append(i)
            # Case 2: current value = top of stack
            elif val == height[stack[-1]]:
                stack.pop()
                stack.append(i)
            # Case 3: current value = top of stack
            elif val > height[stack[-1]]:
                cur_i = 0
                while stack and val > height[stack[-1]]:
                    cur_i = stack.pop()
                    if stack:
                        res += (i - stack[-1] - 1)* (min(height[i], height[stack[-1]]) - height[cur_i])
                stack.append(i)
        return res

print(Solution2().trap( [4,2,0,3,2,5]))
print(Solution().trap( [0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution2().trap( [0,1,0,2,1,0,1,3,2,1,2,1]))

print(Solution().trap( [4,2,3]))
print(Solution2().trap( [4,2,3]))