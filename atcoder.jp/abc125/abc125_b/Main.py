n = int(input())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
dp = [0 for i in range(n+1)] # iまで選んだ時の純利益の最大
for i in range(n):
    dp[i+1] = max(dp[i], dp[i]+a[i]-c[i])
print(dp[n])