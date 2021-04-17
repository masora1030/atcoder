import sys
# from sys import stdin
# readline = stdin.readline
sr = lambda: input()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

import bisect

from sys import stdout

inf = 10 ** 18
mod = 10 ** 9 + 7
# mod = 998244353
# len(bin(n)) - bin(n).rfind("1") - 1

import random

if __name__=='__main__':
    n,p = lr()
    ans = ((p-1)*pow(p-2, n-1, mod))%mod
    print(ans)