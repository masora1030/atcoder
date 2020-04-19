inf = 10**15
mod = 10**9+7

n,m = map(int, input().split())
a = list(map(int, input().split()))
time = sum(a)
if n >= time:
    print(n-time)
else:
    print(-1)