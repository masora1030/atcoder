import sys
import bisect
from collections import deque
import itertools
import math
import heapq
import random

import sys
sys.setrecursionlimit(10**6)
from sys import stdin
# readline = stdin.readline
# sr=lambda: readline()
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n=ir()
    my_e=[[] for i in range(n)]
    e_w = {}
    for i in range(n-1):
        u,v = lr()
        u-=1
        v-=1
        my_e[u].append(v)
        my_e[v].append(u)

    visited = [False for i in range(n)]
    def dfs(root):
        visited[root] = True
        ret_num_nodes = 1
        ret_total_dist = 0
        for next in my_e[root]:
            if not visited[next]:
                num_nodes, total_dist = dfs(next)
                weight = n-2*num_nodes
                ret_num_nodes+=num_nodes
                ret_total_dist+=total_dist+num_nodes
                e_w[root*mod+next]=weight
        return ret_num_nodes, ret_total_dist

    ans = [0 for i in range(n)]
    _, root_dist = dfs(0)
    ans[0] = root_dist

    q = deque([[0, root_dist]])
    while q:
        root, pre_dist = q.popleft()
        for next in my_e[root]:
            if ans[next] == 0:
                ans[next] = pre_dist+e_w[root*mod+next]
                q.append([next, ans[next]])
    for i in range(n):
        print(ans[i])
