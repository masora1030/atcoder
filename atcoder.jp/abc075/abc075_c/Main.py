# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
# list(map(int, list(input()))) # スペースがない数字リストを読み込み
import math
import sys
import bisect
import heapq  # 優先度付きキュー(最小値取り出し)
import collections
from collections import deque

inf = 10**18
mod = 10**9+7

n,m = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(m)]
edge = [[]for k in range(n)]
for i in range(m):
    a,b = ab[i]
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)
ans = 0
for i in range(m): # i番目の編を無視したらどうなるか
    s,g = ab[i]
    s-=1
    g-=1
    visited = [False for j in range(n)]
    q = deque([s])
    while q:
        now = q.popleft()
        visited[now]=True
        for nn in edge[now]:
            if (now!=s or nn!=g) and (not visited[nn]):
                q.append(nn)
    if not all(visited):
        ans += 1
print(ans)