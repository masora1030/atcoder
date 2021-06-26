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
    a=lr()
    a.sort()
    print(a[1]+a[2])