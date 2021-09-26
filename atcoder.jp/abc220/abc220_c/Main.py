import sys
import bisect
from collections import deque
import itertools
import math
import heapq
import random

# import sys
# sys.setrecursionlimit(10**6)
from sys import stdin
# readline = stdin.readline
# sr=lambda: readline()
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n=ir()
    a=lr()
    x=ir()
    a1=[0]
    for num in a:
        a1.append(a1[-1]+num)
    total = sum(a)
    ans = n * (x//total)
    ret = x%total
    ind = bisect.bisect_left(a1, ret)
    if a1[ind] == ret:
        ind+=1
    print(ans+ind)