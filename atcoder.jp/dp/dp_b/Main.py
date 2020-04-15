# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
inf = 10**9+7

n, k = map(int, input().split())
h = list(map(int, input().split()))
dp = [inf for i in range(n+1)]
dp[1] = 0
for i in range(1,n):
    for j in range(k):
        if i-j-1 >= 0:
            dp[i+1] = min(dp[i+1], dp[i-j]+abs(h[i]-h[i-j-1]))
        else:
            break
print(dp[n])