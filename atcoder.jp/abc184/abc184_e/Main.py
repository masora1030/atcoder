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
# mod = 10 ** 9 + 7
mod = 998244353

h,w = lr()
a = [sr() for i in range(h)]
visited = [[inf for j in range(w)] for i in range(h)]
dic = {chr(ord('a')+i):[] for i in range(26)}
visited_a = {chr(ord('a')+i):False for i in range(26)}
sy,sx,gy,gx = 0,0,0,0
for i in range(h):
    for j in range(w):
        if a[i][j] == 'S':
            sy,sx = i,j
        elif a[i][j] == 'G':
            gy,gx = i,j
        elif a[i][j] in dic:
            dic[a[i][j]].append([i,j])
q = deque([[sy,sx,0]])
visited[sy][sx] = 0
dir = [[0,1], [0,-1], [-1,0], [1,0]]
while q:
    y,x,dist = q.popleft()
    for dy,dx in dir:
        ny,nx = y+dy, x+dx
        if 0<=ny<h and 0<=nx<w and visited[ny][nx] == inf and a[ny][nx] != '#':
            visited[ny][nx] = dist+1
            q.append([ny,nx,dist+1])
            if a[ny][nx] == 'G':
                print(dist+1)
                sys.exit()
    if a[y][x] in dic:
        if len(dic[a[y][x]]) > 1 and not visited_a[a[y][x]]:
            visited_a[a[y][x]] = True
            for ny,nx in dic[a[y][x]]:
                if visited[ny][nx] == inf:
                    visited[ny][nx] = dist + 1
                    q.append([ny,nx,dist+1])
print(-1)