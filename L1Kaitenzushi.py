from typing import List


# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    # Write your code here
    prevDishes = [0] * K
    res = 0
    for i in range(N):
        if(D[i] in prevDishes): continue
        else:
            res = res + 1
            prevDishes=prevDishes[1:]+[D[i]]

    return 0
