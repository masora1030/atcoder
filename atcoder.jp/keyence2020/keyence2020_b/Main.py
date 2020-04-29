inf = 10**15
mod = 10**9+7
n = int(input())
rs = [list(map(int, input().split())) for i in range(n)]
rs.sort(key = lambda x : x[0]+x[1])
pre = -inf
ans=0
for i in range(n):
    dis = rs[i][0] - rs[i][1]
    if dis >= pre:
        ans+=1
        pre = rs[i][0] + rs[i][1]
print(ans)