# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
import sys
inf = 10**9+7
mod = 10**9+7

n, d = map(int, input().split())
a,b,c = 0,0,0
while d%2 == 0:
    d //= 2
    a+=1
while d%3 == 0:
    d //= 3
    b+=1
while d%5 == 0:
    d //= 5
    c+=1
if d!=1:
    print(0)
    sys.exit()

dp = [[[[0 for l in range(c+1)]for k in range(b+1)]for j in range(a+1)]for i in range(n+1)]
dp[0][0][0][0] = 1
# 配るDP
for i in range(n): # 1~n回投げる。
    for j in range(a+1): # 2の因数が0からa個
        for k in range(b+1): # 3の因数が0からb個
            for l in range(c+1): # 5の因数が0からc個

                p = dp[i][j][k][l] / 6

                dp[i+1][j][k][l] += p
                dp[i+1][min(a,j+1)][k][l] += p
                dp[i+1][min(a,j+2)][k][l] += p
                dp[i+1][min(a,j+1)][min(b,k+1)][l] += p
                dp[i+1][j][min(b,k+1)][l] += p
                dp[i+1][j][k][min(c,l+1)] += p
print(dp[n][a][b][c])