import sys
import bisect
from collections import deque
import itertools
import math
import heapq
import time
import random
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n,k = lr()
    p = [[sum(lr()),i] for i in range(n)]
    p.sort()
    pp = [num for num, _ in p]
    ans = [False for i in range(n)]
    for pre_s, ind in p:
        max_score = pre_s+300
        max_ind = bisect.bisect_left(pp, max_score)
        if max_ind >= n:
            ans[ind] = True
        while max_ind < n and pp[max_ind] == max_score:
            max_ind+=1
        max_ind-=1
        if max_ind >= n-k:
            ans[ind] = True
    for b in ans:
        if b:
            print("Yes")
        else:
            print("No")
