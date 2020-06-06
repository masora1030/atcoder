inf = 10**18
mod = 10**9+7

n,m = map(int, input().split())
judge = [[False for j in range(n)]for i in range(n)]
for i in range(m):
    x,y = map(int, input().split())
    x -= 1
    y -= 1
    judge[x][y] = True
    judge[y][x] = True
ans = 0
for i in range(1, 2**n):
    use = []
    for j in range(n):
        if ((i >> j) & 1):
            use.append(j)
    leng = len(use)
    flag = True
    for k in range(leng-1):
        for l in range(k+1,leng):
            if not judge[use[k]][use[l]]:
                flag = False
                break
    if flag:
        ans = max(ans, leng)
print(ans)