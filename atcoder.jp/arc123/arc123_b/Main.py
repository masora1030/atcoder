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
mod=10**9+7
# mod = 998244353

if __name__=='__main__':
    n=ir()
    a=lr()
    b=lr()
    c=lr()
    a.sort()
    b.sort()
    c.sort()
    q_b=[]
    q_c=[]
    heapq.heapify(q_b)
    heapq.heapify(q_c)
    ans = 0
    ind_b = 0
    ind_c = 0
    for num in a:
        while ind_b < n and b[ind_b] <= num:
            ind_b+=1
        if ind_b == n:
            break
        num_b = b[ind_b]
        while ind_c < n and c[ind_c] <= num_b:
            ind_c+=1
        if ind_c == n:
            break
        ind_b+=1
        ind_c+=1
        ans+=1
    print(ans)