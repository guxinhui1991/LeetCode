from typing import List


# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
  # Write your code here

  S = sorted(S)
  S_clean = [S[0]]
  for i in range(1, N):
    if S[i] != S[i - 1]: S_clean.append(S[i])

  res = max(S_clean) // 2
  if any(x % 2 == 1 for x in S_clean): res += 1

  return res


print(getMinProblemCount(N = 6, S = [1, 2, 3, 4, 5, 6]))
print(getMinProblemCount(N = 4, S = [4, 3, 3, 4]))
print(getMinProblemCount(N = 4, S = [2, 4, 6, 8]))