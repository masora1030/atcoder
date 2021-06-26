import sys
import bisect
from collections import deque
import itertools

# sys.setrecursionlimit(10**4)
from sys import stdin
readline = stdin.readline
sr=lambda: readline()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
mod=10**9+7
# mod = 998244353

if __name__=='__main__':
    n=ir()
    tlr = [lr() for i in range(n)]
    ans = 0
    for i in range(n-1):
        t,l,r = tlr[i]
        if t == 2:
            r-=0.1
        elif t == 3:
            l+=0.1
        elif t == 4:
            l+=0.1
            r-=0.1
        for j in range(i+1, n):
            tt,ll,rr = tlr[j]
            if tt==2:
                rr-=0.1
            elif tt==3:
                ll+=0.1
            elif tt==4:
                ll+=0.1
                rr-=0.1
            if not (r < ll or rr < l):
                ans+=1
    print(ans)