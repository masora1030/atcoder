import sys
import bisect
import heapq  # 優先度付きキュー(最小値取り出し)


inf = 10 ** 15
mod = 10 ** 9 + 7
n,k = map(int, input().split())
x = list(map(int, input().split()))
minus = []
plus = []
zind = bisect.bisect_left(x, 0)
if zind == n:
    minus = x
    minus.reverse()
else:
    minus = x[0:zind]
    minus.reverse()
    if x[zind] == 0:
        if k == 1:
            print(0)
            sys.exit()
        else:
            n-=1
            k-=1
            plus = x[zind+1:n]
    else:
        plus = x[zind:n]
lenp = len(plus)
lenm = len(minus)
ans = inf
if lenp >= k:
    ans = min(ans, plus[k-1])
if lenm >= k:
    ans = min(ans, abs(minus[k-1]))

for i in range(lenm):
    if 0 <= k-1-(i+1) < lenp:
        ans = min(ans, 2*abs(minus[i])+plus[k-1-(i+1)])
for i in range(lenp):
    if 0 <= k-1-(i+1) < lenm:
        ans = min(ans, 2 * plus[i] + abs(minus[k-1-(i+1)]))

print(ans)