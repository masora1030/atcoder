inf = 10**15
mod = 10**9+7
a,b,c = map(int, input().split())
ans = max(a*10+b+c, b*10+a+c, c*10+b+a)
print(ans)