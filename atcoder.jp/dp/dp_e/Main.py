# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
import sys
inf = 10**9+7
mod = 10**9+7
V = 10**5
n,W = map(int, input().split())
dp = [[inf for j in range(V+1)] for i in range(n+1)]
dp[0][0] = 0
for i in range(n):
    dp[i+1][0] = 0
    w,v = map(int, input().split())
    for j in range(V):
        if j+1-v >= 0:
            dp[i+1][j+1] = min(dp[i][j+1-v]+w, dp[i][j+1])
        else:
            dp[i+1][j+1] = min(dp[i][j+1], w)
for j in range(V+1):
    if dp[n][j] > W:
        print(j-1)
        sys.exit()
        break
print(V)