inf = 10**15
mod = 10**9+7
h,n = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n)]
dp = [[inf for j in range(h+1)] for i in range(n+1)]
for i in range(n):
    dp[i][0] = 0
    a,b = ab[i]
    for j in range(h):
        if j+1-a>=0:
            dp[i+1][j+1] = min(dp[i+1][j+1-a]+b, dp[i][j+1], dp[i][j+1-a]+b)
        else:
            dp[i+1][j+1] = min(dp[i][j+1], b)
print(dp[n][h])