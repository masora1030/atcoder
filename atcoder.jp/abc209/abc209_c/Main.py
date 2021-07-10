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
    c=lr()
    c.sort()
    ans=1
    for i in range(n):
        tmp = i
        ans = ans*max(0, c[i]-tmp)
        ans%=mod
    print(ans)