import sys
import bisect
from collections import deque
import itertools
import math

# sys.setrecursionlimit(10**4)
from sys import stdin
# readline = stdin.readline
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n=ir()*2
    a=lr()
    dp=[[0 for j in range(n+1)] for i in range(n+1)]
    for k in range(2, n+1, 2):
        for l in range(n-k+1):
            r=l+k
            ans = dp[l+1][r-1]+abs(a[l]-a[r-1])
            for i in range(2, k-1, 2):
                ans = min(dp[l][l+i]+dp[l+i][r], ans)
            dp[l][r] = ans
    print(dp[0][n])