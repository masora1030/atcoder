from collections import deque
import pprint
import itertools
import copy
from functools import lru_cache

# input=sys.stdin.buffer.readline

import sys
import random
import time

# from sys import stdin
# readline = stdin.readline
# sr=lambda: readline()
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    n=ir()
    sx,sy,tx,ty = lr()
    xyr = [lr() for _ in range(n)]
    e = [[] for _ in range(n)]
    is_end_cs = [False for _ in range(n)]
    q = deque([])
    visited = set()
    for i in range(n-1):
        x1, y1, r1 = xyr[i]
        for j in range(i+1,n):
            x2, y2, r2 = xyr[j]
            if (x1-x2)**2 + (y1-y2)**2 <= (r1+r2)**2:
                if (x1-x2)**2 + (y1-y2)**2 >= (r1-r2)**2:
                    e[i].append(j)
                    e[j].append(i)
        if (sx-x1)**2 + (sy-y1)**2 == r1**2:
            q.append(i)
            visited.add(i)
        if (tx-x1)**2 + (ty-y1)**2 == r1**2:
            is_end_cs[i] = True
    x1,y1,r1 = xyr[n-1]
    if (sx-x1)**2+(sy-y1)**2==r1**2:
        q.append(n-1)
        visited.add(n-1)
    if (tx-x1)**2+(ty-y1)**2==r1**2:
        is_end_cs[n-1] = True

    while q:
        now = q.popleft()
        if is_end_cs[now]:
            print("Yes")
            sys.exit()
        for next in e[now]:
            if not next in visited:
                q.append(next)
                visited.add(next)

    print("No")

if __name__ == '__main__':
    main()