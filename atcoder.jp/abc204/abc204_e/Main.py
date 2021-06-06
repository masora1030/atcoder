import sys
import bisect
import heapq
import math

# sys.setrecursionlimit(10**4)
# from sys import stdin
# readline = stdin.readline
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

# ダイクストラで始点からの各ノードへのコストを返す (eという配列にstart:[[dist, end], [dist, end]]というエッジを格納)

if __name__=='__main__':
    n,m = lr()
    e=[[] for i in range(n)]
    for k in range(m):
        x, y, c, d = lr()
        e[x-1].append([c, d, y-1])
        e[y-1].append([c, d, x-1])
    def dijkstra(s):
        hq=[(0, s)]
        heapq.heapify(hq)  # リストを優先度付きキューに変換
        cost=[inf for i in range(len(e))]
        cost[s]=0  # 開始地点は0
        while hq:
            c, v=heapq.heappop(hq)
            if c>cost[v]:  # コストが現在のコストよりも高ければスルー
                continue
            for c, d, u in e[v]:
                if d//(cost[v]+1) == 0:
                    tmp=c+cost[v]
                elif d//(cost[v]+1) == 1:
                    tmp=c+1+cost[v]
                elif d//(cost[v]+1) == 2:
                    tmp=c+2+cost[v]
                else:
                    A = cost[v]+1
                    B = d
                    if A*A >= B:
                        tmp = c+(B//A)+cost[v]
                    else:
                        b_s = int(math.sqrt(B))
                        b_ss = b_s+1
                        t = b_s-A
                        pre = t+(B//(A+t))
                        t = b_ss-A
                        pre = min(pre, t+(B//(A+t)))
                        tmp = c+pre+cost[v]
                if tmp<cost[u]:
                    cost[u]=tmp
                    heapq.heappush(hq, (tmp, u))
        return cost
    ss = dijkstra(0)
    if ss[n-1] == inf:
        print(-1)
    else:
        print(ss[n-1])
