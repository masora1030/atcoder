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
w = int(input())
n,k = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n)]
dp = [[[inf for l in range(5001)] for j in range(k+1)] for i in range(n+1)]
for i in range(n+1):
    for j in range(k+1):
        dp[i][j][0] = 0
for i in range(n):
    a,b = ab[i]
    for j in range(k):
        for l in range(5000):
            if l+1-b >= 0:
                dp[i+1][j+1][l+1] = min(dp[i][j][l+1-b]+a, dp[i][j+1][l+1])
            else:
                dp[i+1][j+1][l+1] = dp[i][j+1][l+1]
judge = dp[n][k]
ans = 0
for i,g in enumerate(judge):
    if g <= w:
        ans = max(ans, i)
print(ans)