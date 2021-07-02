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
    n=ir()
    dp = [[0 for j in range(1002)] for i in range(1002)]
    for i in range(n):
        lx, ly, rx, ry = lr()
        dp[lx][ly]+=1
        dp[rx][ry]+=1
        dp[lx][ry]-=1
        dp[rx][ly]-=1
    for i in range(1002):
        for j in range(1001):
            dp[i][j+1]+=dp[i][j]
    for i in range(1002):
        for j in range(1001):
            dp[j+1][i]+=dp[j][i]
    dic = {}
    for i in range(1002):
        for j in range(1002):
            if dp[i][j] in dic:
                dic[dp[i][j]]+=1
            else:
                dic[dp[i][j]]=1
    for i in range(1, n+1):
        if i in dic:
            print(dic[i])
        else:
            print(0)