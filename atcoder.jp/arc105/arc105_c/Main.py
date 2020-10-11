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

n,m = lr()
w = lr()
lv = []
maxw = max(w)
for i in range(m):
    lv.append(lr())
lv.sort(key=lambda x:x[1])
if maxw > lv[0][1]:
    print(-1)
    sys.exit()

max_num = 0
maxl_list = [0]
v_list = []
for l,v in lv:
    max_num = max(max_num, l)
    maxl_list.append(max_num)
    v_list.append(v)

jun = [i for i in range(n)]
ans = inf
for juns in itertools.permutations(jun):
    w1 = [0]
    for num in juns:
        w1.append(w1[-1]+w[num])
    def sumArea(l, r):
        return w1[r] - w1[l]

    dist = [[0 for i in range(n)] for j in range(n)]
    for i in range(n-1):
        for j in range(i+1,n):
            tmp = sumArea(i,j+1)
            ind = bisect.bisect_left(v_list, tmp)
            dist[i][j] = maxl_list[ind]

    ans_tmp = 0
    dp = [0 for i in range(n+1)] # i番目まで見たときの最大距離
    for i in range(n-1):
        tmp = 0
        for j in range(i+1):
            tmp = max(tmp, dp[j]+dist[j][i+1])
        dp[i+1] = tmp
    ans_tmp = dp[n-1]
    ans = min(ans_tmp, ans)
print(ans)
