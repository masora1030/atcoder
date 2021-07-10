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
    n,x = lr()
    a = lr()
    total = 0
    for i in range(n):
        if i%2 == 1:
            total+=(a[i]-1)
        else:
            total+=a[i]
    if x >= total:
        print("Yes")
    else:
        print("No")