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
    n,k = lr()
    a=lr()
    lis = [[a[i],i] for i in range(n)]
    lis.sort()
    ans = k//n
    ret = k%n
    is_add = [False for i in range(n)]
    for j in range(ret):
        ind = lis[j][1]
        is_add[ind] = True
    for i in range(n):
        if is_add[i]:
            print(ans+1)
        else:
            print(ans)