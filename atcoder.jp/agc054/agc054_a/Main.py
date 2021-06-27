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
mod=10**9+7
# mod = 998244353

if __name__=='__main__':
    n=ir()
    s=sr()
    if s[0] != s[-1]:
        print(1)
        sys.exit()
    pre = s[0]
    d = s[0]
    for c in s:
        if c != d and pre != d:
            print(2)
            sys.exit()
        pre = c
    print(-1)