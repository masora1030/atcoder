import sys
sys.setrecursionlimit(10**9)                    #再帰の深さブースト

n = int(input())
edge = [[] for i in range(n)]
ans = [0 for i in range(n)]
for i in range(n-1):
    u,v,w = map(int, input().split())
    edge[u-1].append([v-1,w%2])
    edge[v-1].append([u-1,w%2])

def bfsC(pre, now, nowc):
    for node, weight in edge[now]:
        if node != pre:
            if weight:
                ans[node] = 1-nowc
                bfsC(now, node, 1-nowc)
            else:
                ans[node] = nowc
                bfsC(now, node, nowc)
bfsC(-1, 0, 0)
for i in range(n):
    print(ans[i])