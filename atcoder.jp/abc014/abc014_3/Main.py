inf = 10 ** 15
mod = 10 ** 9 + 7
n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
judgep = [0 for i in range(10**6+1)]
judgem = [0 for i in range(10**6+2)]
dp = [0 for i in range(10**6+1)]
for a,b in ab:
    judgep[a]+=1
    judgem[b+1]+=1
dp[0] = judgep[0]
ans = dp[0]
for i in range(10**6):
    dp[i+1] = dp[i]+judgep[i+1]-judgem[i+1]
    ans = max(ans,dp[i+1])
print(ans)