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
mod=10**9+7
# mod = 998244353

if __name__=='__main__':
    a=lr()
    s1=a[1]-a[0]
    s2=a[2]-a[1]
    ans=0
    if s2 - s1 > 1:
        ans+=(s2-s1)//2
        s1+=ans
        s2-=ans
    if s2 - s1 == 1:
        print(ans+2)
    else:
        ans+=abs(s1-s2)
        print(ans)