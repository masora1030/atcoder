inf = 10**15
mod = 10**9+7

n,m,x = map(int, input().split())
san = [list(map(int, input().split())) for i in range(n)]
ans = inf
for i in range(2**n):
    cost = 0
    judge = [0 for i in range(m)]
    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # 1だったら(オンだったら)
            for k in range(m):
                judge[k] += san[j][k+1]
            cost+=san[j][0]
    flag = True
    for l in range(m):
        if judge[l] < x:
            flag = False
            break
    if flag:
        ans = min(ans,cost)
if ans == inf:
    print(-1)
else:
    print(ans)