import itertools
import math
import heapq
import random

# import sys
# sys.setrecursionlimit(10**6)
from sys import stdin
# readline = stdin.readline
# sr=lambda: readline()
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
mod=10**9+7
# mod = 998244353

if __name__=='__main__':
    test = ir()
    for t in range(test):
        n2, n3, n4 = lr()
        ans = 0
        sousa = [[5,0,0], [2,2,0], [3,0,1], [0,2,1], [1,0,2]]
        for lis in itertools.permutations(sousa):
            pre = 0
            ret2, ret3, ret4 = n2, n3, n4
            for d2, d3, d4 in lis:
                tmp = inf
                if d2 != 0:
                    tmp = min(tmp, ret2//d2)
                if d3 != 0:
                    tmp = min(tmp, ret3//d3)
                if d4 != 0:
                    tmp = min(tmp, ret4//d4)
                pre+=tmp
                ret2-=tmp*d2
                ret3-=tmp*d3
                ret4-=tmp*d4
            ans = max(ans, pre)
        print(ans)