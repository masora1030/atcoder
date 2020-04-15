# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
inf = 10**9+7

n,W = map(int, input().split())
dp = [[0 for j in range(W+1)] for i in range(n+1)] # i個まで選んだ時の最大値

for i in range(n):
    w, v = map(int, input().split())
    for j in range(W):
        if j+1-w >= 0:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i][j+1-w]+v)
        else:
            dp[i+1][j+1] = dp[i][j+1]
print(dp[n][W])