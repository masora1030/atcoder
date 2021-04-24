import sys

# sys.setrecursionlimit(10**4)
# from sys import stdin
# readline = stdin.readline
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

import bisect

from sys import stdout

inf=10**18
mod=10**9+7
# mod = 998244353
# len(bin(n)) - bin(n).rfind("1") - 1

import random


if __name__=='__main__':
    n = ir()
    a = lr()
    b = lr()
    x_min = 1
    x_max = 1000
    for i in range(n):
        x_min = max(x_min, a[i])
        x_max = min(x_max, b[i])
    print(max(0,x_max-x_min+1))