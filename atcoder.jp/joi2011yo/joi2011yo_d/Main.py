# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
import sys
inf = 10**9+7
mod = 10**9+7

n = int(input())
a = list(map(int, input().split()))

b = a[-1]
# i個目までで計算結果がjとなる数
dp = [[0 for j in range(21)] for i in range(n)]
dp[0][0] = 1
dp[1][a[0]] = 1
for i in range(1,n-1):
    for j in range(21):
        if j - a[i] >= 0 and j + a[i] <= 20:
            dp[i+1][j] = dp[i][j-a[i]]+dp[i][j+a[i]]
        elif 0 <= j - a[i]:
            dp[i+1][j] = dp[i][j-a[i]]
        elif j + a[i] <= 20:
            dp[i+1][j] = dp[i][j+a[i]]
        else:
            dp[i+1][j] = 0
print(dp[n-1][b])