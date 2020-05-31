# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
import math
import sys
import bisect
import heapq  # 優先度付きキュー(最小値取り出し)
from collections import deque
inf = 10 ** 15
mod = 10 ** 9 + 7
n,a,b = map(int, input().split())
if b <= a:
    print(b*(n-1))
    sys.exit()
x = list(map(int, input().split()))
dp = [inf for i in range(n+1)] # iにつく時の最小の消費量
dp[1] = 0
for i in range(1,n):
    dp[i+1] = dp[i] + min((x[i]-x[i-1])*a, b)
print(dp[n])