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

a = [input() for i in range(10)]
sh,sw = 0,0
total = 0
for h in range(10):
    for w in range(10):
        if a[h][w] == 'o':
            sh, sw = h, w
            total+=1

def dfsCount(th, tw):
    ret = 0
    visited = [[False for w in range(10)]for i in range(10)]
    q = deque([[sh,sw]])
    visited[sh][sw] = True
    while q:
        nh, nw = q.popleft()
        ret+=1
        for dh,dw in [[-1,0], [1,0], [0,-1], [0,1]]:
            if (0 <= nh+dh < 10 and 0 <= nw+dw < 10 and a[nh+dh][nw+dw] == 'o' and (not visited[nh+dh][nw+dw])) or (nh+dh == th and nw+dw == tw and (not visited[nh+dh][nw+dw])):
                q.append([nh+dh, nw+dw])
                visited[nh+dh][nw+dw] = True
    return ret

flag = False
for h in range(10):
    for w in range(10):
        if a[h][w] == 'x' and (a[h][max(w-1,0)] == 'o' or a[max(h-1,0)][w] == 'o' or a[min(h+1,9)][w] == 'o' or a[h][min(w+1,9)] == 'o'):
            if dfsCount(h,w) == total+1:
                flag = True
                break
    if flag:
        break
if flag:
    print('YES')
else:
    print('NO')
