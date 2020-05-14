inf = 10 ** 15
mod = 10 ** 9 + 7

n,m,q = map(int, input().split())

maps = [[0 for j in range(n)]for i in range(n)]
for i in range(m):
    l,r = map(int, input().split())
    l-=1
    r-=1
    maps[l][r]+=1
c = []
for i in range(n):
    a = [0]
    for j in maps[i]: a.append(a[-1]+j)
    c.append(a)
for i in range(q):
    l,r  = map(int, input().split())
    ans = 0
    for i in range(l-1,r):
        ans += (c[i][r]-c[i][l-1])
    print(ans)