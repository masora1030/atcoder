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
n, m = map(int, input().split())
# 幅優先？
ans = [-1 for i in range(n)]  # i+1番目の部屋にある道しるべ
visited = [False for i in range(n)]
visited[0] = True
dicab = {}
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a in dicab.keys():
        dicab[a].append(b)
        if b in dicab.keys():
            dicab[b].append(a)
        else:
            dicab[b] = [a]
    else:
        dicab[a] = [b]
        if b in dicab.keys():
            dicab[b].append(a)
        else:
            dicab[b] = [a]


def bfs():
    q = deque([0])
    while q:
        now = q.popleft()
        nlist = dicab[now]
        for nextnode in nlist:
            if visited[nextnode] == False:
                visited[nextnode] = True
                ans[nextnode] = now
                q.append(nextnode)


bfs()
ans[0] = 0
print('Yes')
for i in range(1, n):
    print(ans[i] + 1)