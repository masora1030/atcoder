inf = 10**9+7

n = int(input())
dp = [inf for i in range(n+1)]
dp[0] = 0
tmp = 1
use = [1]
while tmp*6 <= n:
    tmp *= 6
    use.append(tmp)
tmp = 1
while tmp*9 <= n:
    tmp *= 9
    use.append(tmp)
use.sort()

for i in range(n):
    for num in use:
        if i+1-num >= 0:
            dp[i+1] = min(dp[i+1], dp[i+1-num]+1)
        else:
            break
print(dp[n])