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

# import numpy as np

if __name__=='__main__':
    n=ir()
    s = lr()
    ok = []
    for a in range(1,500):
        for b in range(1, 500):
            ok.append(4*a*b+3*a+3*b)
    ok.sort()
    ans = 0
    for num in s:
        ind = bisect.bisect_left(ok,num)
        if ok[ind] != num:
            ans+=1
    print(ans)
