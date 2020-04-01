n,m = map(int, input().split())
break_stair = [False for i in range(n)]
for i in range(m):
    break_stair[int(input())-1] = True
mod = 10**9+7
# i番目にたどり着く総数
dp = [0 for i in range(n+1)]
dp[0] = 1
if break_stair[0]:
    dp[1] = 0
else:
    dp[1] = 1
for i in range(n-1):
    if break_stair[i+1]:
        dp[i+2] = 0
    else:
        dp[i+2] = (dp[i] + dp[i+1])%mod
print(dp[n])