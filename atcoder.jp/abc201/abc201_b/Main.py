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
    n = ir()
    a = [sr().split() for i in range(n)]
    inds = [[int(num[1]),i] for i,num in enumerate(a)]
    inds.sort(reverse=True)
    print(a[inds[1][1]][0])