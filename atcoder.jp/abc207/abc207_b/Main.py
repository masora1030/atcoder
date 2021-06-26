import sys
import bisect
from collections import deque
import itertools

# sys.setrecursionlimit(10**4)
from sys import stdin
readline = stdin.readline
sr=lambda: readline()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
mod=10**9+7
# mod = 998244353

if __name__=='__main__':
    a,b,c,d = lr()
    if c*d-b <= 0:
        print(-1)
    else:
        tmp = c*d-b
        print((a+tmp-1)//tmp)