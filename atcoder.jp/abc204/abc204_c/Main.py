import sys
import bisect
import heapq

# sys.setrecursionlimit(10**4)
# from sys import stdin
# readline = stdin.readline
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n,m = lr()
    e = [[] for i in range(n)]
    for i in range(m):
        a,b = lr()
        a-=1
        b-=1
        e[a].append([1,b])
    ans = 0
    def dijkstra(s):
        hq=[(0, s)]
        heapq.heapify(hq)  # リストを優先度付きキューに変換
        cost=[inf for i in range(len(e))]
        cost[s]=0
        while hq:
            c, v=heapq.heappop(hq)
            if c>cost[v]:  # コストが現在のコストよりも高ければスルー
                continue
            for d, u in e[v]:
                tmp=d+cost[v]
                if tmp<cost[u]:
                    cost[u]=tmp
                    heapq.heappush(hq, (tmp, u))
        return cost
    for num in range(n):
        ss = dijkstra(num)
        for cost in ss:
            if cost < inf:
                ans+=1
    print(ans)