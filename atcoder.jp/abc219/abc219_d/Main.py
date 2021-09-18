import sys
import bisect
from collections import deque
import itertools
import math
import heapq
import random

# import sys
# sys.setrecursionlimit(10**6)
from sys import stdin
# readline = stdin.readline
# sr=lambda: readline()
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
mod=10**9+7
# mod = 998244353

if __name__=='__main__':
    n=ir()
    x,y=lr()
    ab = []
    a_t, b_t = 0,0
    for i in range(n):
        a,b = lr()
        a_t+=a
        b_t+=b
        ab.append([a,b])
    ab.sort(key=lambda x: x[0]+x[1])
    if a_t < x or b_t < y:
        print(-1)
        sys.exit()
    dp = [[[inf for j in range(y+1)] for i in range(x+1)] for k in range(n+1)] # k コマで見た時、i 以上, j 以上 を実現する最小の個数
    for k in range(n+1):
        dp[k][0][0]=0
    for k in range(n):
        a,b = ab[k]
        for i in range(x+1):
            for j in range(y+1):
                dp[k+1][i][j] = min(dp[k][i][j], dp[k][max(0,i-a)][max(0,j-b)]+1)
    print(dp[n][x][y])
