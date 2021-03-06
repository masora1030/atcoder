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
# mod = 10 ** 9 + 7
mod = 998244353
n = ir()
s = sr()
dp = [['S', 'S'],['S', 'W'],['W', 'S'],['W', 'W']]
dpp = [['S', 'W'],['W', 'S'],['W', 'S'],['S', 'W']]

for k in range(4):
    for i in range(1,n):
        if s[i] == 'o':
            if dp[k][i] == 'S':
                if dp[k][i-1] == 'S':
                    dp[k].append('S')
                else:
                    dp[k].append('W')
            else:
                if dp[k][i-1] == 'S':
                    dp[k].append('W')
                else:
                    dp[k].append('S')
        else:
            if dp[k][i] == 'S':
                if dp[k][i-1] == 'S':
                    dp[k].append('W')
                else:
                    dp[k].append('S')
            else:
                if dp[k][i-1] == 'S':
                    dp[k].append('S')
                else:
                    dp[k].append('W')

    if s[0] == 'o':
        if dp[k][-2] == dpp[k][0] and dp[k][-1] == dp[k][0]:
            print(*dp[k][:-1], sep='')
            sys.exit()
    else:
        if dp[k][-2] == dpp[k][1] and dp[k][-1] == dp[k][0]:
            print(*dp[k][:-1], sep='')
            sys.exit()

print(-1)