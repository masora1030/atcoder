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

n,m = map(int, input().split())
ab = [[] for i in range(8)]
for i in range(m):
    a,b = map(int, input().split())
    ab[a-1].append(b-1)
    ab[b-1].append(a-1)


def dfs(visited, now):
    tmp = [visited[i] for i in range(n)]
    tmp[now] = True
    if all(tmp):
        return 1
    else:
        ret = 0
        for b in ab[now]:
            if not tmp[b]:
                ret+=dfs(tmp, b)
        return ret

print(dfs([False for i in range(n)], 0))