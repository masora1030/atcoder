inf = 10**15
mod = 10**9+7
n,T = map(int, input().split())
minc = inf
for i in range(n):
    c,t = map(int, input().split())
    if t <= T:
        minc = min(minc, c)
if minc == inf:
    print('TLE')
else:
    print(minc)