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

import time
import random
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

# import numpy as np

if __name__=='__main__':
    n,s = lr()
    ab = [lr() for i in range(n)]
    judge_dp = [[False for i in range(s+1)] for j in range(n+1)]
    judge_dp[0][0] = True
    for i in range(n):
        a,b = ab[i]
        for j in range(s+1):
            if j-a >= 0 and judge_dp[i][j-a]:
                judge_dp[i+1][j] = True
            if j-b >= 0 and judge_dp[i][j-b]:
                judge_dp[i+1][j] = True
    if not judge_dp[n][s]:
        print("Impossible")
        sys.exit()
    ans = []
    retS = s
    for i in range(n):
        a, b = ab[n-1-i]
        if retS-a >= 0 and judge_dp[n-1-i][retS-a]:
            ans.append("A")
            retS-=a
        elif retS-b >= 0 and judge_dp[n-1-i][retS-b]:
            ans.append("B")
            retS-=b
    ans.reverse()
    print("".join(ans))