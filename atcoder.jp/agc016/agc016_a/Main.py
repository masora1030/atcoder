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

s = input()
#アルファベット
al=[chr(ord('a') + i) for i in range(26)]
ans = inf
for c in al:
    pre = 0
    maxpre = 0
    for now in s:
        if c == now:
            maxpre = max(pre, maxpre)
            pre = 0
        else:
            pre += 1
    maxpre = max(pre, maxpre)
    ans = min(ans, maxpre)
print(ans)