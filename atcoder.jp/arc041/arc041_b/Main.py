# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
# list(map(int, list(input()))) # スペースがない数字リストを読み込み
import math
import sys
import bisect
import heapq  # 優先度付きキュー(最小値取り出し)
from collections import deque
inf = 10**18
mod = 10**9+7

# a^n
def power(a,n,mod):
    x = 1
    while n:
        if n & 1:
            x *= a % mod
        n >>= 1
        a *= a % mod
    return x % mod


n,m = map(int, input().split())
b = [list(map(int, list(input()))) for i in range(n)]
ans = [[0 for j in range(m)] for i in range(n)]
for i in range(1,n-1):
    for j in range(1,m-1):
        tmp = min(b[i][j - 1], b[i][j + 1], b[i + 1][j], b[i - 1][j])
        if tmp > 0:
            ans[i][j] = tmp
            b[i][j - 1] -= tmp
            b[i][j + 1] -= tmp
            b[i + 1][j] -= tmp
            b[i - 1][j] -= tmp

for i in range(n):
    print(*ans[i], sep='')