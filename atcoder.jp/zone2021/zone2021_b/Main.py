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

if __name__=='__main__':
    n,D,H= lr()
    ans = 0
    for i in range(n):
        d,h = lr()
        y = (D*h-H*d)/(H-h)
        x = y*H/(D+y)
        ans = max(x,ans)
    print(ans)