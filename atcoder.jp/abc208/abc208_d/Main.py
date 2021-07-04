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
    n,m = lr()
    e = []
    w = []
    ans=0
    dist=[[inf for j in range(n)] for i in range(n)]
    for i in range(n):
        dist[i][i]=0

    for i in range(m):
        a, b, c=lr()
        a-=1
        b-=1
        dist[a][b]=c

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j]=min(dist[i][j], dist[i][k]+dist[k][j])
        for i in range(n):
            for j in range(n):
                if dist[i][j] != inf:
                    ans+=dist[i][j]
    print(ans)