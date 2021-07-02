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
    T=ir()
    l,x,y = lr()
    q=ir()
    for _ in range(q):
        t=ir()
        s=3/2*math.pi - 2*math.pi*t/T
        cos = math.cos(s)
        sin = math.sin(s)
        tmp = math.sqrt(x**2+(l/2*cos-y)**2)
        tmp1 = l/2*(1+sin)
        ans = math.atan2(tmp1, tmp)
        ans = ans/(2*math.pi)*360
        print(ans)