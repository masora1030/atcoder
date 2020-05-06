inf = 10**15
mod = 10**9+7
n = int(input())
ans=0
dp = [[0 for j in range(10)]for i in range(10)]
for k in range(1,n+1):
    tmp = str(k)
    dp[int(tmp[0])][int(tmp[-1])]+=1
for i in range(1,10):
    for j in range(1,10):
        ans+=dp[i][j]*dp[j][i]
print(ans)