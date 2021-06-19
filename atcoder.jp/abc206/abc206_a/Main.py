import sys
import bisect
from collections import deque
import itertools

# sys.setrecursionlimit(10**4)
# from sys import stdin
# readline = stdin.readline
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
mod=10**9+7
# mod = 998244353

if __name__=='__main__':
    n=ir()
    if int(n*1.08) < 206:
        print("Yay!")
    elif int(n*1.08) == 206:
        print("so-so")
    else:
        print(":(")