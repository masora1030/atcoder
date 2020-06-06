inf = 10**18
mod = 10**9+7

k = int(input())
dp = [0 for i in range(41)]
dp[0] = 1
dp[1] = 1
for i in range(2, 41):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[k-1], dp[k])