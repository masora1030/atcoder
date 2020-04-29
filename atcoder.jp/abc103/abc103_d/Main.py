inf = 10**15
mod = 10**9+7
n,m = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(m)]
ab.sort(key=lambda x:x[1])
pre = -inf
ans=0
for tmp in ab:
    a,b = tmp
    if a >= pre:
        ans+=1
        pre=b
print(ans)