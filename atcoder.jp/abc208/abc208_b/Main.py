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
    p=ir()
    lis = [1]
    ans = 0
    for i in range(2,11):
        lis.append(lis[-1]*i)
    ret = p
    while ret > 0:
        ind = bisect.bisect_left(lis, ret)
        if ind == 10:
            ret-=lis[-1]
            ans+=1
        else:
            if lis[ind] == ret:
                ret-=lis[ind]
                ans+=1
            else:
                ret-=lis[ind-1]
                ans+=1
    print(ans)