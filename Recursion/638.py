from typing import List


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        res = []

        len_price = len(price)
        special.sort(key=lambda x: x[-1])
        i = 0
        while i < len(special)-1:
            s1, s2 = special[i][:-1], special[i+1][:-1]
            p1, p2 = special[i][-1], special[i+1][-1]
            if p2>=p1>0 and all([s2[idx]==s1[idx] for idx in range(len_price)]):
                del special[i+1]
                continue
            elif 0<p2<=p1 and all([s2[idx]==s1[idx] for idx in range(len_price)]):
                del special[i]
                continue
            i+=1


        def dfs(need_cur, res_crr):
            nonlocal price
            if any(v<0 for v in need_cur): return
            #if not all(v>0 for v in need_cur):
            res.append(res_crr + sum(x * max(0,y) for x, y in zip(price, need_cur)))

            for i,val in enumerate(special):
                dfs([need_cur[i] - val[:-1][i] for i in range(len(need_cur))], res_crr + val[-1])

            return


        dfs(needs, 0)

        return min(res)



print(Solution().shoppingOffers(price = [4,9,6], special = [[2,3,2,1],[1,2,1,7],[1,0,0,2]], needs = [4,5,3]))
print(Solution().shoppingOffers(price = [1,1,1], special = [[1,1,0,4],[2,2,1,0]], needs = [1,1,1]))
print(Solution().shoppingOffers(price = [9], special =[[1,10],[2,2]], needs =[3]))
print(Solution().shoppingOffers(price = [2,2], special =[[1,1,1],[1,1,2],[1,1,3],[1,1,4],[1,1,5],[1,1,6],[1,1,7],[1,1,8],[1,1,9],[1,1,10],[1,1,11],[1,1,12],[1,1,13],[1,1,14],[1,1,15]], needs =[10,10]))

print(Solution().shoppingOffers(price = [1,1,1], special =[[1,1,0,0],[2,2,1,9]], needs =[1,1,0]))
print(Solution().shoppingOffers(price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]))
