import sys
import bisect
from collections import deque
import itertools
import math
import heapq

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
    n,k = lr()
    LR = ['' for i in range(n)]
    for i in range(k):
        c,kk = input().split()
        LR[int(kk)-1] = c
    ok = [0 for i in range(n)]
    nums = k
    for i,c in enumerate(LR):
        if c == '':
            ok[i] = nums
        elif c == 'R':
            ok[i] = 1
            nums-=1
        else:
            ok[i] = 1
    lind = 0
    for i in range(n):
        c = LR[n-1-i]
        if c == 'L':
            lind+=1
        elif c == '':
            ok[n-1-i]-=lind
    ans = 1
    for num in ok:
        ans*=num
        ans%=mod
    print(ans)