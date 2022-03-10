class SegmentTree:
    def __init__(self, size, f=lambda x, y: x+y, default=0):
        self.size=2**(size-1).bit_length()
        self.default=default
        self.dat=[default]*(self.size*2)
        self.f=f

    def update(self, i, x):
        i+=self.size
        self.dat[i]=x
        while i>0:
            i>>=1
            self.dat[i]=self.f(self.dat[i*2], self.dat[i*2+1])

    def query(self, l, r):
        l+=self.size
        r+=self.size
        lres, rres=self.default, self.default
        while l<r:
            if l & 1:
                lres=self.f(lres, self.dat[l])
                l+=1

            if r & 1:
                r-=1
                rres=self.f(self.dat[r], rres)
            l>>=1
            r>>=1
        res=self.f(lres, rres)
        return res


# import sys
# sys.setrecursionlimit(10**6)

import random
import math
import fractions
import sys
import bisect
import random
import time
import heapq  # 優先度付きキュー(最小値取り出し)
import collections
from collections import Counter
from collections import deque
import pprint
import itertools
import copy
from functools import lru_cache

import sys

# input=sys.stdin.buffer.readline

# from sys import stdin
# readline = stdin.readline
# sr=lambda: readline()
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

import sys

inf=10**18
# mod = 10**9+7
mod=998244353

if __name__=='__main__':
    n=ir()
    a=lr()
    b=lr()
    ab=[[a[i],b[i]] for i in range(n)]
    b.sort()
    ab.sort(key=lambda x:x[1], reverse=True)
    ab.sort(key=lambda x:x[0])
    sorted_b = [ab[i][1] for i in range(n)]
    num2ind = {}
    ind = 0
    for num in b:
        if not num in num2ind:
            num2ind[num] = ind
            ind+=1
    nums = ind
    seg = SegmentTree(nums, lambda x, y: x+y, 0)
    ans = 0
    for i in range(n-1, -1, -1):
        num = sorted_b[i]
        ind = num2ind[num]
        seg.update(ind, seg.query(ind, ind+1)+1)
        ans += seg.query(0,ind+1)
    others = {}
    for num1, num2 in ab:
        if (num1, num2) in others:
            others[(num1, num2)]+=1
        else:
            others[(num1, num2)]=1
    for _, v in others.items():
        ans += v*(v-1)//2
    print(ans)
