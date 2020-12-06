sr = lambda: input()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

mod = 10 ** 9 + 7
# mod = 998244353

import sys
sys.setrecursionlimit(10**7)

h,w = lr()
a = [lr() for i in range(h)]
cost = [[0 for j in range(w)] for i in range(h)]

visited = [[False for j in range(w)] for i in range(h)]

def getCost(i,j):
    if visited[i][j]:
        return cost[i][j]

    ret = 1
    if 0<=i-1 and a[i-1][j] > a[i][j]:
        ret += getCost(i-1, j)
    if 0<=j-1 and a[i][j-1] > a[i][j]:
        ret += getCost(i, j-1)
    if i+1<h and a[i+1][j] > a[i][j]:
        ret += getCost(i+1, j)
    if j+1<w and a[i][j+1] > a[i][j]:
        ret += getCost(i, j+1)
    ret = ret%mod
    cost[i][j] = ret
    visited[i][j] = True
    return ret


for ny in range(h):
    for nx in range(w):
        if visited[ny][nx]:
            continue

        # 幅優先しつつcostを埋めていく
        getCost(ny,nx)
        visited[ny][nx] = True

ans = 0
for i in range(h):
    for j in range(w):
        ans = (ans+cost[i][j])%mod

print(ans)