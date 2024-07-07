import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        val_map = {}
        for i in range(len(nums)):
            if nums[i] in val_map:
                val_map[nums[i]] += 1
            else:
                val_map[nums[i]] = 1

        heap = [(val, key) for key, val in val_map.items()]
        res_val = heapq.nlargest(k, heap)

        return [i[1] for i in res_val]

nums = [1,1,1,2,2,3]
k = 2
Solution().topKFrequent(nums, k)