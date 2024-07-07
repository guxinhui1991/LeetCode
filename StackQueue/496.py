from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:


        def nextGreaterIndex(arr):

            N = len(arr)
            res = [-1 for _ in range(N)]
            stack = []
            for i in range(N):
                while stack and arr[i]>arr[stack[-1]]:
                    cur_i = stack.pop()
                    res[cur_i] = arr[i]
                stack.append(i)
            return res

        def findIndex(i, arr):
            if i in arr:
                return arr.index(i)
            else:
                return -1

        next_great_nums2 = nextGreaterIndex(nums2)
        # res = []
        # for val in nums1:
        #     index_in_nums2 = findIndex(val, nums2)
        #     next_great_element = next_great_nums2[index_in_nums2]
        #     res.append(next_great_element)

        return [next_great_nums2[findIndex(val, nums2)] for val in nums1]


    def nextGreaterElement_optimized(self, nums1: List[int], nums2: List[int]) -> List[int]:

        def nextGreaterIndex(arr):
            N = len(arr)
            map_nums = {}
            stack = []
            for i in range(N):
                while stack and arr[i]>arr[stack[-1]]:
                    cur_i = stack.pop()
                    map_nums[cur_i] = arr[i]
                stack.append(i)
            return map_nums

        def indexValMap(arr):
            map_nums = {}
            for i in range(len(arr)):
                map_nums[arr[i]] = i
            return map_nums


        next_great_nums2 = nextGreaterIndex(nums2)
        val_index_map = indexValMap(nums2)
        return [next_great_nums2[val_index_map[val]] if val_index_map[val] in next_great_nums2 else -1 for val in nums1]

print(Solution().nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))
print(Solution().nextGreaterElement_optimized(nums1 = [4,1,2], nums2 = [1,3,4,2]))