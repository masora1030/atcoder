# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
inf = 10**9+7
mod = 10**9+7

n = int(input())
p = list(map(int, input().split()))
dp = [[0 for j in range(10001)] for i in range(n+1)] # iまでみた時に得点合計がjの時1

for i in range(n):
    dp[i][0] = 1
    dp[i+1][0] = 1
    pnow = p[i]
    for j in range(10000):
        if j+1-pnow >=0:
            dp[i+1][j+1] = max(dp[i][j+1-pnow], dp[i+1][j+1], dp[i][j+1])
        else:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1])
print(sum(dp[n]))