from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
  # Write your code here
  S = sorted(S)
  S_clean =[S[0]]
  for i in range(1, N):
    if S[i] != S[i-1]: S_clean.append(S[i])

  if len(S_clean) < 2 : return minQ(S_clean[0])

  dp = [0 for _ in range(len(S_clean))]
  dp[0] = minQ(S_clean[0])
  dp[1] = min(minQ(S_clean[1]), dp[0] + minQ(S_clean[1] - S_clean[0]))

  for i in range(2, len(S_clean)):
      dp[i] = min(dp[i-1] + minQ(S_clean[i] - S_clean[i-1]), dp[i-2] + minQ(S_clean[i] - S_clean[i-2]))

  return dp[-1]

def minQ(number):
  return min(number//2 + number%2, number//3 + number%3)

print(getMinProblemCount(N = 6, S = [1, 2, 3, 4, 5, 6]))
print(getMinProblemCount(N = 4, S = [4, 3, 3, 4]))
print(getMinProblemCount(N = 4, S = [2, 4, 6, 8]))