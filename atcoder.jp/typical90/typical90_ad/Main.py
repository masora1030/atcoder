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
    n,k = lr()
    c = [0 for i in range(n+1)]
    for i in range(2, n+1):
        if c[i] != 0:
            continue
        else:
            for j in range(i, n+1, i):
                c[j]+=1
    ans=0
    for num in c:
        if num >= k:
            ans+=1
    print(ans)