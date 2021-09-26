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
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n=ir()
    a=lr()
    dp = [[0 for i in range(10)] for j in range(n)]
    dp[0][a[0]] = 1
    for i in range(n-1):
        ne = a[i+1]
        for j in range(10):
            dp[i+1][(j*ne)%10] += dp[i][j]
            dp[i+1][(j+ne)%10] += dp[i][j]
        for j in range(10):
            dp[i+1][j]%=mod
    for j in range(10):
        print(dp[n-1][j])