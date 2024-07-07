from itertools import accumulate as acc
from math import inf

A =[3,5,1,3,9,8]
B = A[::-1]
K = 4
N = len(A)


def solution(A, K):
    pre = zip(acc(A, min, initial=inf),
              acc(A, max, initial=-inf))
    suf = list(zip(list(acc(A[::-1], min, initial=inf))[::-1],
                    list(acc(A[::-1], max, initial=-inf))[::-1]))
    return min(max(left[1], right[1]) - min(left[0], right[0])
               for left, right in zip(pre, suf[K:]))

print(solution(A, K))