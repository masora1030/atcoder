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

sr = lambda: input()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

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
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

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

inf = 10 ** 18
mod = 10 ** 9 + 7
# mod = 998244353
h,w = lr()
s = [sr() for i in range(h)]
dir = [[1,0], [0,1], [1,1]]
maps = [[0 for i in range(w)] for j in range(h)]
maps[0][0] = 1
if s[0][1] == '.':
    maps[0][1] = 1
if s[1][0] == '.':
    maps[1][0] = 1
for i in range(2,h):
    if s[i][0] != '#':
        maps[i][0] = maps[i-1][0]*2%mod
    else:
        break
for i in range(2,w):
    if s[0][i] != '#':
        maps[0][i] = maps[0][i-1]*2%mod
    else:
        break
off = w-1
nanamesam = []
tatesam = []
yokosam = []
for i in range(h):
    yokosam.append(maps[i][0])
for j in range(w):
    tatesam.append(maps[0][j])
for i in range(h+w-1):
    if i < w:
        nanamesam.append(maps[0][w-i-1])
    else:
        nanamesam.append(maps[i-w+1][0])

for i in range(h-1):
    for j in range(w-1):
        if s[i+1][j+1] != '#':
            if 0<=i and 0<=j:
                maps[i+1][j+1] = (maps[i+1][j+1]+nanamesam[i-j+off])%mod
            if 0<=i:
                maps[i+1][j+1] = (maps[i+1][j+1]+tatesam[j+1])%mod
            if 0<=j:
                maps[i+1][j+1] = (maps[i+1][j+1]+yokosam[i+1])%mod
            nanamesam[i - j + off] = (nanamesam[i - j + off] + maps[i + 1][j + 1]) % mod
            tatesam[j+1] = (tatesam[j+1]+maps[i+1][j+1])%mod
            yokosam[i+1] = (yokosam[i+1]+maps[i+1][j+1])%mod
        else:
            nanamesam[i-j+off]=0
            tatesam[j + 1] = 0
            yokosam[i + 1] = 0
print(maps[h-1][w-1])