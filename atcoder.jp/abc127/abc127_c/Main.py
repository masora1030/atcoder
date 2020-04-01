n,m = map(int, input().split())
Lmin = 0
Rmax = n
for i in range(m):
    L,R = map(int, input().split())
    Lmin = max(L-1, Lmin)
    Rmax = min(R, Rmax)
if Lmin < Rmax:
    ans = Rmax - Lmin
else:
    ans = 0
print(ans)