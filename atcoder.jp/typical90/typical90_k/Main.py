import sys
import bisect

# sys.setrecursionlimit(10**4)
# from sys import stdin
# readline = stdin.readline
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
mod=10**9+7
# mod = 998244353

if __name__=='__main__':
    n = ir()
    dcs = [lr() for i in range(n)]
    dcs.sort()
    max_d = dcs[-1][0]

    dp = [[0 for j in range(max_d+1)] for i in range(n+1)]

    for i in range(n):
        d,c,s = dcs[i]
        for j in range(d):
            if j+1-c >= 0:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1], dp[i][j+1-c]+s)
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    print(dp[n][max_d])