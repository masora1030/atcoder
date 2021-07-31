import sys
import bisect
from collections import deque
import itertools
import math
import heapq
import random

# sys.setrecursionlimit(10**4)
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
    n,m,k = lr()
    e = [[i] for i in range(n)]
    for i in range(m):
        a,b = lr()
        a-=1
        b-=1
        e[a].append(b)
        e[b].append(a)
    dp = [[0 for j in range(n)] for i in range(k+1)] # 残りi日の時点でjで取れる通り数
    dp[0][0] = 1 # 最後は1
    total = 1
    for i in range(k):
        pre_total=0
        for j in range(n):
            pre = total
            for num in e[j]:
                pre-=dp[i][num]
            pre%=mod
            dp[i+1][j] = pre
            pre_total+=pre
        pre_total%=mod
        total = pre_total
    print(dp[k][0])