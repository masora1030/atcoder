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
from collections import deque
import pprint

# a^n
def power(a,n,mod):
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
    tmp = n-1
    while(tmp >= l):
        a = a*tmp%mod
        tmp -= 1
    return a

inf = 10**18
mod = 10**9+7

n,m = map(int, input().split())
if abs(n-m) > 1:
    print(0)
    sys.exit()
if n%2 == m%2:
    print(kaijo(n,1,mod)*kaijo(m,1,mod)*2%mod)
else:
    print(kaijo(n, 1, mod) * kaijo(m, 1, mod)%mod)