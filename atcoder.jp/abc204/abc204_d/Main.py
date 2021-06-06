import sys
import bisect

# sys.setrecursionlimit(10**4)
# from sys import stdin
# readline = stdin.readline
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n=ir()
    a=lr()
    total = sum(a)//2
    dp = [[0 for i in range(total+1)] for j in range(n+1)]
    for i in range(n):
        num = a[i]
        for j in range(total):
            if j+1-num >= 0:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i][j+1-num]+num)
            else:
                dp[i+1][j+1] = dp[i][j+1]
    ans = 0
    for num in range(total+1):
        ans = max(ans, dp[n][num])
    print(sum(a)-ans)