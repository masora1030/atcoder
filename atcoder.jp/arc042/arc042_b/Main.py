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


inf = 10 ** 18
mod = 10 ** 9 + 7

x,y = lr()
n = ir()
xy = []
ans = inf
for i in range(n):
    xy.append(lr())
for i in range(n):
    x1,y1 = xy[i]
    x2,y2 = xy[(i+1)%n]
    a,b,c = 0,0,0
    if x1-x2 == 0:
        a = 1
        c = -x1
    elif y1-y2 == 0:
        b = 1
        c = -y1
    else:
        c = (y1-((y1-y2)*x1/(x1-x2)))*(x1-x2)
        a = y1-y2
        b = x2-x1
    ans = min(ans, abs(a*x+b*y+c)/math.sqrt(a**2 + b**2))
print(ans)