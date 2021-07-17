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
    n,k=lr()
    a=lr()
    dic={}
    ind=0
    for num in a:
        if not num in dic:
            dic[num]=ind
            ind+=1
    nums = [0 for i in range(ind)]
    ans = 0
    for i in range(k):
        num = dic[a[i]]
        if nums[num] == 0:
            ans+=1
        nums[num]+=1
    kind = ans
    for i in range(n-k):
        popnum = dic[a[i]]
        pushnum = dic[a[i+k]]
        nums[popnum]-=1
        if nums[popnum] == 0:
            kind-=1
        nums[pushnum]+=1
        if nums[pushnum] == 1:
            kind+=1
        ans = max(kind, ans)
    print(ans)