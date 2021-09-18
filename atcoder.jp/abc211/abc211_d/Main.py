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
    n,m = lr()

    ed = [[] for i in range(n)]
    for _ in range(m):
        a,b = lr()
        a-=1
        b-=1
        ed[a].append(b)
        ed[b].append(a)
    q = deque([[0,0]])
    cnt = [[1, inf] for i in range(n)]
    cnt[0][1] = 0
    while q:
        c, d = q.popleft()
        nd = d+1
        for num in ed[c]:
            if cnt[num][1] > nd:
                cnt[num][1] = nd
                cnt[num][0] = cnt[c][0]
                q.append([num, nd])
            elif cnt[num][1] == nd:
                cnt[num][0] += cnt[c][0]
            cnt[num][0]%=mod
    if cnt[n-1][1] != inf:
        print(cnt[n-1][0])
    else:
        print(0)