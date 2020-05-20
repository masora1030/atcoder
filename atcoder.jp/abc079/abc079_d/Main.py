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

h,w = map(int, input().split())
c = [list(map(int, input().split())) for i in range(10)]
for a in range(10):
    for i in range(10):
        for j in range(10):
            if i != j:
                for k in range(10):
                    c[i][j] = min(c[i][j], c[i][k]+c[k][j])
a = [list(map(int, input().split())) for i in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        if a[i][j] != -1:
            ans+=c[a[i][j]][1]
print(ans)

