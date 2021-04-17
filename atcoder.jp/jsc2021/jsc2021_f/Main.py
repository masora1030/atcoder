# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
# list(map(int, list(input()))) # スペースがない数字リストを読み込み
import math
import fractions
import sys
import bisect
import heapq  # 優先度付きキュー(最小値取り出し)
import collections
from collections import Counter
from collections import deque
import pprint
import itertools
from functools import lru_cache

"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""
def factorization(n):
    arr = []
    temp = n
    if n == 1:
        return arr

    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


# a^n
def power(a, n, mod):
    x = 1
    while n:
        if n & 1:
            x *= a % mod
        n >>= 1
        a *= a % mod
    return x % mod


# n*(n-1)*...*(l+1)*l
def kaijo(n, l, mod):
    if n == 0:
        return 1
    a = n
    tmp = n - 1
    while (tmp >= l):
        a = a * tmp % mod
        tmp -= 1
    return a

# Union Find
class UnionFind():
    def __init__(self, n):
        self.n=n
        self.parents=[-1]*n

    def find(self, x):
        if self.parents[x]<0:
            return x
        else:
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x=self.find(x)
        y=self.find(y)

        if x==y:
            return

        if self.parents[x]>self.parents[y]:
            x, y=y, x

        self.parents[x]+=self.parents[y]
        self.parents[y]=x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x)==self.find(y)

    def members(self, x):
        root=self.find(x)
        return [i for i in range(self.n) if self.find(i)==root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x<0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

    def all_family_count(self):
        return [-min(0, x) for i, x in enumerate(self.parents)]

    def memberlist(self):
        self.L=[set() for _ in range(self.n)]
        for i in range(self.n):
            if self.parents[i]<0:
                self.L[i].add(i)
            else:
                self.L[self.find(i)].add(i)
        return self.L

# 約数生成
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


# segment tree
class SegmentTree:
    # 初期化処理
    # f : SegmentTreeにのせるモノイド
    # default : fに対する単位元
    def __init__(self, size, f=lambda x, y: x+y, default=0):
        self.size=2**(size-1).bit_length()  # 簡単のため要素数Nを2冪にする
        self.default=default
        self.dat=[default]*(self.size*2)  # 要素を単位元で初期化
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
                rres=self.f(self.dat[r], rres)  # モノイドでは可換律は保証されていないので演算の方向に注意
            l>>=1
            r>>=1
        res=self.f(lres, rres)
        return res

import sys
# sys.setrecursionlimit(10**4)
# from sys import stdin
# readline = stdin.readline
sr = lambda: input()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

import bisect

from sys import stdout

inf = 10 ** 18
mod = 10 ** 9 + 7
# mod = 998244353
# len(bin(n)) - bin(n).rfind("1") - 1

import random


# segment tree

class SegmentTree:
    # 初期化処理
    # f : SegmentTreeにのせるモノイド
    # default : fに対する単位元
    def __init__(self, size, f, default):
        self.size=2**(size-1).bit_length()  # 簡単のため要素数Nを2冪にする
        self.default=default
        self.dat=[default]*(self.size*2)  # 要素を単位元で初期化
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
                rres=self.f(self.dat[r], rres)  # モノイドでは可換律は保証されていないので演算の方向に注意
            l>>=1
            r>>=1
        res=self.f(lres, rres)
        return res


if __name__=='__main__':
    n,m,q = lr()

    txy = [lr() for i in range(q)]
    dic = {}
    for t,x,y in txy:
        if not y in dic:
            dic[y] = 0
    dic_num_ind = {0:0}
    a_num = [0 for i in range(n)]
    b_num = [0 for i in range(m)]
    for i,k in enumerate(sorted(dic.keys())):
        dic_num_ind[k] = i+1

    ans = 0
    sega = SegmentTree(len(dic_num_ind), lambda x, y: [x[0]+y[0], x[1]+y[1]], [0,0])
    sega.update(0, [n,0])
    segb=SegmentTree(len(dic_num_ind), lambda x, y: [x[0]+y[0], x[1]+y[1]], [0,0])
    segb.update(0, [m,0])

    for t,x,y in txy:
        x-=1
        ind_num = dic_num_ind[y]
        if t==1:
            pre=a_num[x]
            a_num[x]=y
            ind_pre=dic_num_ind[pre]

            pre_nums = sega.query(ind_pre,ind_pre+1)[0]-1
            y_nums = sega.query(ind_num, ind_num+1)[0]+1
            sega.update(ind_pre, [pre_nums, pre*pre_nums])
            sega.update(ind_num, [y_nums, y*y_nums])

            ans-=pre*segb.query(0,ind_pre+1)[0]
            ans-=segb.query(ind_pre+1,len(dic_num_ind))[1]
            ans+=y*segb.query(0,ind_num+1)[0]
            ans+=segb.query(ind_num+1,len(dic_num_ind))[1]

        else:
            pre=b_num[x]
            b_num[x]=y
            ind_pre=dic_num_ind[pre]

            pre_nums=segb.query(ind_pre, ind_pre+1)[0]-1
            y_nums=segb.query(ind_num, ind_num+1)[0]+1
            segb.update(ind_pre, [pre_nums, pre*pre_nums])
            segb.update(ind_num, [y_nums, y*y_nums])

            ans-=pre*sega.query(0, ind_pre+1)[0]
            ans-=sega.query(ind_pre+1, len(dic_num_ind))[1]
            ans+=y*sega.query(0, ind_num+1)[0]
            ans+=sega.query(ind_num+1, len(dic_num_ind))[1]

        print(ans)
