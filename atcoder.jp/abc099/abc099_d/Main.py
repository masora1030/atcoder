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


inf = 10 ** 18
mod = 10 ** 9 + 7

n,k = lr()
d = [lr() for i in range(k)]
c = [lr() for i in range(n)]
ans = [0 for i in range(3)]
pre = inf
fir = []
sec = []
thr = []
firkouho = []
seckouho = []
thrkouho = []
for y in range(n):
    for x in range(n):
        if (y + x) % 3 == 0:
            fir.append(c[y][x]-1)
        elif (y + x) % 3 == 1:
            sec.append(c[y][x]-1)
        else:
            thr.append(c[y][x] - 1)

for i in range(k):
    ans[0] = 0
    for ind in fir:
        ans[0] += d[ind][i]
    firkouho.append([ans[0], i])

for i in range(k):
    ans[1] = 0
    for ind in sec:
        ans[1] += d[ind][i]
    seckouho.append([ans[1], i])

for i in range(k):
    ans[2] = 0
    for ind in thr:
        ans[2] += d[ind][i]
    thrkouho.append([ans[2], i])

firkouho.sort()
seckouho.sort()
thrkouho.sort()

for i in range(k):
    ans[0] = 0
    ans[0],ind1 = firkouho[i]
    for j in range(k):
        if seckouho[j][1] != ind1:
            ans[1] = 0
            ans[1],ind2 = seckouho[j]
            for l in range(k):
                if thrkouho[l][1] != ind1 and thrkouho[l][1] != ind2:
                    ans[2] = 0
                    ans[2],ind3 = thrkouho[l]
                    pre = min(pre,sum(ans))
print(pre)