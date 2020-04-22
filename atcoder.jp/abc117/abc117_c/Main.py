inf = 10**9+7
mod = 10**9+7
n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
sub = []
for i in range(m-1):
    sub.append(x[i+1]-x[i])
sub.sort()
for i in range(n-1):
    if sub:
        sub.pop()
if sub:
    print(sum(sub))
else:
    print(0)