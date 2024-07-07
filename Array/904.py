class Solution(object):
    def totalFruit(self, fruits):

        l = r = total = cur = r_count = 0
        for i in fruits:
            cur = cur+1 if i in (l, r) else r_count + 1
            r_count = r_count + 1 if i == r else 1
            if i != r : l, r = r, i
            total = max(total, cur)
        return total



class Solution2(object):
    def totalFruit2(self, fruits):
        cur = {}
        l, N = 0, len(fruits)
        res = 0
        for r, f in enumerate(fruits):
            cur[f] = cur.get(f, 0) + 1
            while len(cur) > 2:
                cur[fruits[l]] -= 1
                if cur[fruits[l]] == 0: del cur[fruits[l]]
                l += 1
            res = max(r-l+1, res)
        return res 

print(Solution().totalFruit([0,1,6,6,4,4,6]))
print(Solution().totalFruit([0,1,6,6,4,4,6]))
print(Solution2().totalFruit2([0,1,2,2]))
print(Solution2().totalFruit2([0,1,2,2]))
