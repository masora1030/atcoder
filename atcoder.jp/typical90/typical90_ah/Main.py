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
    a = lr()
    dic = {}
    ind = 0
    for num in sorted(a):
        if num in dic:
            continue
        else:
            dic[num]=ind
            ind+=1
    a = [dic[num] for num in a]
    def judge(mid):
        inc = [0 for i in range(ind)]
        now_count = 0
        for i in range(mid):
            num = a[i]
            if inc[num]:
                inc[num] += 1
            else:
                inc[num] = 1
                now_count += 1
        if now_count <= k:
            return True
        for i in range(1, n-mid+1):
            de = a[i-1]
            if inc[de] == 1:
                now_count-=1
            inc[de]-=1
            st = a[i+mid-1]
            if inc[st] == 0:
                now_count+=1
            inc[st]+=1
            if now_count <= k:
                return True
        return False

    l = k
    r = n+1
    while r-l > 1:
        mid = (l+r)//2
        if judge(mid):
            l = mid
        else:
            r = mid
    print(l)
